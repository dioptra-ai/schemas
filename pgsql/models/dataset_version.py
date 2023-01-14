from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, String, Boolean, text, func
from sqlalchemy.schema import Index, ForeignKey

from .base import Base

class DatasetVersion(Base):
    __tablename__ = "dataset_versions"

    uuid = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    organization_id = Column(String(), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(String(), nullable=False)
    display_name = Column(String())
    is_current = Column(Boolean(), nullable=False, server_default=text('true'))
    root_parent_uuid = Column(UUID(as_uuid=True), ForeignKey('dataset_versions.uuid'), nullable=True)

    def __repr__(self):
        return f"DatasetVersion(uuid={self.uuid!r}, created_at={self.timestamp!r})"

Index('datasets_organization_id_index', DatasetVersion.organization_id)
