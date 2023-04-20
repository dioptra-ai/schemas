import enum
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy import Column, String, text, Enum
from sqlalchemy.schema import ForeignKey, UniqueConstraint, CheckConstraint, Index

from .base import Base

class FeatureVectorType(enum.Enum):
    EMBEDDINGS = "EMBEDDINGS"
    LOGITS = "LOGITS"
    PXL_ENTROPY = "PXL_ENTROPY"
    PXL_VARIANCE = "PXL_VARIANCE"
    GRAD_EMBEDDINGS = "GRAD_EMBEDDINGS"

class FeatureVector(Base):
    __tablename__ = "feature_vectors"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    organization_id = Column(String(), nullable=False)
    type = Column(Enum(FeatureVectorType), nullable=False)
    prediction = Column(UUID(as_uuid=True), ForeignKey('predictions.id', ondelete='CASCADE'), nullable=False)
    bbox = Column(UUID(as_uuid=True), ForeignKey('bboxes.id', ondelete='CASCADE'), nullable=True)
    encoded_value = Column(String(), nullable=True)

    # Ideas:
    # Store each vector in its own S3 file.
    #   Storage costs for 10M datapoints at 1MB each: 10,000GB * $0.023 = $230/month
    #   S3 doesn't allow bulk operations (read/write), so we'd be charged for each request.
    #       Price for 100,000 vectors = 100,000 * 0.0004 / 1000 = $0.04
    #       Data transfer price $0 if in the same region.
    # Use S3 Select queries to get the feature vector from an S3 file with multiple vectors. Needs proper partitioning. Use this metadata to store a pointer to the S3 file.
    # Use pyarrow and parquet to store the vectors in S3.
    # Use dynamodDB.
    #   Storage costs for 10M datapoints at 1MB each: $1000/month - $2,500/month depending on storage class (Standard vs Infrequent Access)
    #   Read costs for 100,000 * 1MB vectors eventually consistent: ~$10-$20 per request => oops...
    #
    # {
    #    "s3": {
    #       "bucket": "bucket-name",
    #       "key": "path/to/file.parquet",

    #   },
    #   "postgres": {
    #       "table": "events",
    #       "column": "embeddings",
    #       "uuid": "uuid-of-datapoint"
    #   }
    # }
    metadata_ = Column('metadata', JSONB(), nullable=True)

    # User-provided model and version identification.
    # If we want our own ids later, we can use "model" and "model_version" as foreign keys and remove this.
    # Using '' as default to have the unique constraint work in the absence of a model_name.
    model_name = Column(String(), nullable=False, server_default=text("''"))

    def __repr__(self):
        return f"FeatureVector(id={self.id}, organization_id={self.organization_id}, type={self.type}, prediction={self.prediction}, encoded_value?{bool(self.encoded_value)}, metadata={self.metadata_}, model_name={self.model_name})"

Index('feature_vector_organization_id_index', FeatureVector.organization_id)
Index('feature_vector_type_index', FeatureVector.type)
Index('feature_vector_model_name_index', FeatureVector.model_name)
Index('feature_vector_prediction_index', FeatureVector.prediction)
Index('feature_vector_bbox_index', FeatureVector.bbox)

# There should be only one feature vector per prediction, type and model_name.
UniqueConstraint(FeatureVector.prediction, FeatureVector.model_name, FeatureVector.type, name='feature_vectors_prediction_model_name_type_unique')
# There should be only one feature vector per bbox, type and model_name.
UniqueConstraint(FeatureVector.bbox, FeatureVector.model_name, FeatureVector.type, name='feature_vectors_bbox_model_name_type_unique')