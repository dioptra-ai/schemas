from sqlalchemy.dialects.postgresql import UUID, ARRAY, JSONB
from sqlalchemy import Column, DateTime, String, text, Enum, func, Float
from sqlalchemy.schema import ForeignKey, UniqueConstraint, Index

from .base import Base
from .groundtruth import TaskType

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    organization_id = Column(String(), nullable=False)
    datapoint = Column(UUID(as_uuid=True), ForeignKey('datapoints.id', ondelete='CASCADE'), nullable=False)
    task_type = Column(Enum(TaskType), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    class_name = Column(String(), nullable=True)
    class_names = Column(ARRAY(String()), nullable=True)
    confidence = Column(Float(), nullable=True)
    confidences = Column(ARRAY(Float()), nullable=True)
    top = Column(Float(), nullable=True)
    left = Column(Float(), nullable=True)
    height = Column(Float(), nullable=True)
    width = Column(Float(), nullable=True)
    metrics = Column(JSONB, nullable=True)
    # User-provided model and version identification.
    # If we want our own ids later, we can use "model" and "model_version" as foreign keys and remove this.
    model_name = Column(String(), nullable=True)

    def __repr__(self):
        return f"Prediction(id={self.id!r}, datapoint={self.datapoint!r}, task_type={self.task_type!r})"

Index('predictions_organization_id_index', Prediction.organization_id)
Index('predictions_datapoint_index', Prediction.datapoint)
Index('predictions_task_type_index', Prediction.task_type)
Index('predictions_created_at_index', Prediction.created_at)
Index('predictions_class_name_index', Prediction.class_name)
Index('predictions_class_names_index', Prediction.class_names)
Index('predictions_confidence_index', Prediction.confidence)
Index('predictions_confidences_index', Prediction.confidences)
Index('predictions_top_index', Prediction.top)
Index('predictions_left_index', Prediction.left)
Index('predictions_width_index', Prediction.width)
Index('predictions_height_index', Prediction.height)
Index('predictions_metrics_index', Prediction.metrics)
Index('predictions_model_name_index', Prediction.model_name)

# There should be only one prediction per datapoint and model_name
UniqueConstraint(Prediction.datapoint, Prediction.model_name, name='predictions_datapoint_model_name_unique')
