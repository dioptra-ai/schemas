from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, String, text, Enum, func
from sqlalchemy.schema import ForeignKey, UniqueConstraint, Index

from .base import Base
from .groundtruth import TaskType

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    organization_id = Column(String(), nullable=False)
    datapoint = Column(UUID(as_uuid=True), ForeignKey('datapoints.id'), nullable=False)
    task_type = Column(Enum(TaskType), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    # User-provided model and version identification.
    # If we want our own ids later, we can use "model" and "model_version" as foreign keys and remove this.
    model_name = Column(String(), nullable=True)

    def __repr__(self):
        return f"Prediction(id={self.id!r}, datapoint={self.datapoint!r}, task_type={self.task_type!r})"

Index('predictions_organization_id_index', Prediction.organization_id)

# There should be only one prediction per datapoint and model_name
UniqueConstraint(Prediction.datapoint, Prediction.model_name, name='predictions_datapoint_model_name_unique')
