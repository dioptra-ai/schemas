import enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, text, Enum, func, DateTime
from sqlalchemy.schema import ForeignKey, Index

from .base import Base

class TaskType(enum.Enum):
    OBJECT_DETECTION = "OBJECT_DETECTION"
    CLASSIFICATION = "CLASSIFICATION"
    NER = "NER"

class GroundTruth(Base):
    __tablename__ = "groundtruths"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    organization_id = Column(String(), nullable=False)
    datapoint = Column(UUID(as_uuid=True), ForeignKey('datapoints.id'), nullable=False)
    task_type = Column(Enum(TaskType), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    def __repr__(self):
        return f"GroundTruth(id={self.id!r}, datapoint={self.datapoint!r})"

Index('groundtruths_organization_id_index', GroundTruth.organization_id)
