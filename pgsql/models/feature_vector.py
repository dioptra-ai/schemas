import enum
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy import Column, String, text, Enum
from sqlalchemy.schema import ForeignKey, UniqueConstraint, CheckConstraint, Index

from .base import Base

class FeatureVectorType(enum.Enum):
    EMBEDDINGS = "EMBEDDINGS"
    LOGITS = "LOGITS"

class FeatureVector(Base):
    __tablename__ = "feature_vectors"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    organization_id = Column(String(), nullable=False)
    name = Column(Enum(FeatureVectorType), nullable=False)
    datapoint = Column(UUID(as_uuid=True), ForeignKey('datapoints.id'), nullable=True)
    prediction = Column(UUID(as_uuid=True), ForeignKey('predictions.id'), nullable=True)
    value = Column(JSONB(), nullable=True)
    metadata_ = Column('metadata', JSONB(), nullable=True)

    # User-provided model and version identification.
    # If we want our own ids later, we can use "model" and "model_version" as foreign keys and remove this.
    model_name = Column(String(), nullable=True)

    def __repr__(self):
        return f"FeatureVector(id={self.id!r}, datapoint={self.datapoint!r}, url={self.url!r})"

Index('feature_vector_organization_id_index', FeatureVector.organization_id)

# There should be only one feature vector per datapoint and model_name.
UniqueConstraint(FeatureVector.datapoint, FeatureVector.model_name, name='feature_vectors_datapoint_model_name_unique')
# There should be only one feature vector per prediction and model_name.
UniqueConstraint(FeatureVector.prediction, FeatureVector.model_name, name='feature_vectors_prediction_model_name_unique')

# Either datapoint or prediction should be set.
CheckConstraint(
    (FeatureVector.datapoint != None) | (FeatureVector.prediction != None),
    name='feature_vectors_datapoint_or_prediction_set'
)
