from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy import Column, DateTime, String, text, func, Float, CheckConstraint
from sqlalchemy.schema import ForeignKey, Index

from .base import Base

class Prompt_Response(Base):
    __tablename__ = "prompt_responses"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    organization_id = Column(String(), nullable=False)
    prediction = Column(UUID(as_uuid=True), ForeignKey('predictions.id', ondelete='CASCADE'), nullable=True)
    groundtruth = Column(UUID(as_uuid=True), ForeignKey('groundtruths.id', ondelete='CASCADE'), nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    confidence = Column(Float(), nullable=True)
    metrics = Column(JSONB, nullable=True)
    prompt = Column(String(), nullable=True)
    context = Column(String(), nullable=True)
    response = Column(String(), nullable=True)
    def __repr__(self):
        return f"Prompt_Response(id={self.id!r}, prediction={self.prediction!r}, groundtruth={self.groundtruth!r}, confidence={self.confidence!r}), coco_polyline={self.coco_polyline!r}"

Index('prompt_responses_organization_id_index', Prompt_Response.organization_id)
Index('prompt_responses_prediction_index', Prompt_Response.prediction)
Index('prompt_responses_groundtruth_index', Prompt_Response.groundtruth)
Index('prompt_responses_confidence_index', Prompt_Response.confidence)

# Either prediction is not null XOR groundtruth is not null.
# CheckConstraint('(prediction IS NULL AND groundtruth IS NOT NULL) OR (prediction IS NOT NULL AND groundtruth IS NULL)', name='prompt_responses_prediction_xor_groundtruth_not_null')
CheckConstraint(
    (Prompt_Response.prediction.is_(None) & Prompt_Response.groundtruth.isnot(None)) | (Prompt_Response.prediction.isnot(None) & Prompt_Response.groundtruth.is_(None)),
    name='prompt_responses_prediction_xor_groundtruth_not_null'
)
# Confidence is null for groundtruths.
CheckConstraint(
    Prompt_Response.groundtruth.is_(None) | (Prompt_Response.groundtruth.isnot(None) & Prompt_Response.confidence.is_(None)),
    name='prompt_responses_groundtruth_confidence_null'
)
# CheckConstraint('NOT (groundtruth IS NOT NULL and confidence IS NOT NULL)', name='prompt_responses_groundtruth_confidence_null')