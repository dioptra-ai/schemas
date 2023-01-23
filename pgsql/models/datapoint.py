from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, String, text, func
from sqlalchemy.schema import Index, UniqueConstraint

from .base import Base

class Datapoint(Base):
    __tablename__ = "datapoints"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    organization_id = Column(String(), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())

    request_id = Column(String(), nullable=False)

    def __repr__(self):
        return f"Datapoint(id={self.id!r}, created_at={self.timestamp!r})"

Index('datapoints_organization_id_index', Datapoint.organization_id)
Index('datapoints_request_id_index', Datapoint.request_id)
UniqueConstraint(Datapoint.organization_id, Datapoint.request_id, name='datapoints_organization_id_request_id_unique')
