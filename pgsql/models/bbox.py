from sqlalchemy.dialects.postgresql import UUID, ARRAY, JSONB
from sqlalchemy import Column, DateTime, String, text, func, Float, CheckConstraint
from sqlalchemy.schema import ForeignKey, Index

from .base import Base

class BBox(Base):
    __tablename__ = "bboxes"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    organization_id = Column(String(), nullable=False)
    prediction = Column(UUID(as_uuid=True), ForeignKey('predictions.id', ondelete='CASCADE'), nullable=True)
    groundtruth = Column(UUID(as_uuid=True), ForeignKey('groundtruths.id', ondelete='CASCADE'), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    class_name = Column(String(), nullable=True)
    class_names = Column(ARRAY(String()), nullable=True)
    confidence = Column(Float(), nullable=True)
    confidences = Column(ARRAY(Float()), nullable=True)
    encoded_resized_segmentation_mask = Column(String(), nullable=True)
    encoded_segmentation_mask = Column(String(), nullable=True)
    top = Column(Float(), nullable=True)
    left = Column(Float(), nullable=True)
    height = Column(Float(), nullable=True)
    width = Column(Float(), nullable=True)
    metrics = Column(JSONB, nullable=True)

    def __repr__(self):
        return f"BBox(id={self.id!r}, prediction={self.prediction!r}, groundtruth={self.groundtruth!r} class_name={self.class_name!r}, confidence={self.confidence!r}, top={self.top!r}, left={self.left!r}, height={self.height!r}, width={self.width!r})"

Index('bboxes_organization_id_index', BBox.organization_id)
Index('bboxes_prediction_index', BBox.prediction)
Index('bboxes_groundtruth_index', BBox.groundtruth)
Index('bboxes_class_name_index', BBox.class_name)
Index('bboxes_confidence_index', BBox.confidence)

# Either prediction is not null XOR groundtruth is not null.
# CheckConstraint('(prediction IS NULL AND groundtruth IS NOT NULL) OR (prediction IS NOT NULL AND groundtruth IS NULL)', name='bboxes_prediction_xor_groundtruth_not_null')
CheckConstraint(
    (BBox.prediction.is_(None) & BBox.groundtruth.isnot(None)) | (BBox.prediction.isnot(None) & BBox.groundtruth.is_(None)),
    name='bboxes_prediction_xor_groundtruth_not_null'
)
# Confidence is null for groundtruths.
CheckConstraint(
    BBox.groundtruth.is_(None) | (BBox.groundtruth.isnot(None) & BBox.confidence.is_(None)),
    name='bboxes_groundtruth_confidence_null'
)
# CheckConstraint('NOT (groundtruth IS NOT NULL and confidence IS NOT NULL)', name='bboxes_groundtruth_confidence_null')
