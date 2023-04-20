from sqlalchemy.dialects.postgresql import UUID, ARRAY, JSONB
from sqlalchemy import Column, DateTime, String, text, func, Float, CheckConstraint
from sqlalchemy.schema import ForeignKey, Index

from .base import Base

class Lane(Base):
    __tablename__ = "lanes"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    organization_id = Column(String(), nullable=False)
    prediction = Column(UUID(as_uuid=True), ForeignKey('predictions.id', ondelete='CASCADE'), nullable=True)
    groundtruth = Column(UUID(as_uuid=True), ForeignKey('groundtruths.id', ondelete='CASCADE'), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    confidence = Column(Float(), nullable=True)
    coco_polyline = Column(ARRAY(Float()), nullable=True)

    def __repr__(self):
        return f"Lane(id={self.id!r}, prediction={self.prediction!r}, groundtruth={self.groundtruth!r}, confidence={self.confidence!r}), coco_polyline={self.coco_polyline!r}"

Index('lanes_organization_id_index', Lane.organization_id)
Index('lanes_prediction_index', Lane.prediction)
Index('lanes_groundtruth_index', Lane.groundtruth)
Index('lanes_confidence_index', Lane.confidence)

# Either prediction is not null XOR groundtruth is not null.
# CheckConstraint('(prediction IS NULL AND groundtruth IS NOT NULL) OR (prediction IS NOT NULL AND groundtruth IS NULL)', name='lanes_prediction_xor_groundtruth_not_null')
CheckConstraint(
    (Lane.prediction.is_(None) & Lane.groundtruth.isnot(None)) | (Lane.prediction.isnot(None) & Lane.groundtruth.is_(None)),
    name='lanes_prediction_xor_groundtruth_not_null'
)
# Confidence is null for groundtruths.
CheckConstraint(
    Lane.groundtruth.is_(None) | (Lane.groundtruth.isnot(None) & Lane.confidence.is_(None)),
    name='lanes_groundtruth_confidence_null'
)
# CheckConstraint('NOT (groundtruth IS NOT NULL and confidence IS NOT NULL)', name='lanes_groundtruth_confidence_null')