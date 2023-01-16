from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, String, Boolean, text, func
from sqlalchemy.schema import Index, ForeignKey

from .base import Base

class Dataset(Base):
    __tablename__ = "datasets"

    uuid = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    organization_id = Column(String(), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(String(), nullable=False)
    display_name = Column(String(), nullable=False)

    def __repr__(self):
        return f"Dataset(uuid={self.uuid!r}, created_at={self.timestamp!r})"

Index('actual_datasets_organization_id_index', Dataset.organization_id)
