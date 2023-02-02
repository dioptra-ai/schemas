import enum
import uuid
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy import Column, DateTime, String, text, func, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Index, UniqueConstraint

from .base import Base

class DatapointType(enum.Enum):
    IMAGE = "IMAGE"
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"
    TEXT = "TEXT"

class Datapoint(Base):
    __tablename__ = "datapoints"

    # This so that client-side unpersisted objects receive a UUID.
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.id = uuid.uuid4()

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    organization_id = Column(String(), nullable=False)
    # TODO: migrate existing event data, populate this and and make it non-nullable.
    type = Column(Enum(DatapointType), nullable=True)
    metadata_ = Column('metadata', JSONB, nullable=True)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    # TODO: remove this later.
    request_id = Column(String(), nullable=True)

    def __repr__(self):
        return f"Datapoint(id={self.id!r}, created_at={self.created_at!r}, type={self.type!r})"

Index('datapoints_organization_id_index', Datapoint.organization_id)
