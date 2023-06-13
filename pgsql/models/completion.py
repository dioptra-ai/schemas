from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy import Column, DateTime, String, text, func, Float, CheckConstraint
from sqlalchemy.schema import ForeignKey, Index

from .base import Base

class Completion(Base):
    __tablename__ = "completions"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    organization_id = Column(String(), nullable=False)
    prediction = Column(UUID(as_uuid=True), ForeignKey('predictions.id', ondelete='CASCADE'), nullable=True)
    groundtruth = Column(UUID(as_uuid=True), ForeignKey('groundtruths.id', ondelete='CASCADE'), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    confidence = Column(Float(), nullable=True)
    metrics = Column(JSONB, nullable=True)
    text = Column(String(), nullable=True)
    def __repr__(self):
        return f"Completion(id={self.id!r}, prediction={self.prediction!r}, groundtruth={self.groundtruth!r}, confidence={self.confidence!r}), coco_polyline={self.coco_polyline!r}"

Index('completions_organization_id_index', Completion.organization_id)
Index('completions_prediction_index', Completion.prediction)
Index('completions_groundtruth_index', Completion.groundtruth)
Index('completions_confidence_index', Completion.confidence)

# Either prediction is not null XOR groundtruth is not null.
# CheckConstraint('(prediction IS NULL AND groundtruth IS NOT NULL) OR (prediction IS NOT NULL AND groundtruth IS NULL)', name='completions_prediction_xor_groundtruth_not_null')
CheckConstraint(
    (Completion.prediction.is_(None) & Completion.groundtruth.isnot(None)) | (Completion.prediction.isnot(None) & Completion.groundtruth.is_(None)),
    name='completions_prediction_xor_groundtruth_not_null'
)
# Confidence is null for groundtruths.
CheckConstraint(
    Completion.groundtruth.is_(None) | (Completion.groundtruth.isnot(None) & Completion.confidence.is_(None)),
    name='completions_groundtruth_confidence_null'
)
# CheckConstraint('NOT (groundtruth IS NOT NULL and confidence IS NOT NULL)', name='completions_groundtruth_confidence_null')