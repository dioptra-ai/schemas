from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column
from sqlalchemy.schema import ForeignKey

from .base import Base

# Dataset lineage: a dataset version can have multiple parents, and multiple children.
class DatasetVersionLine(Base):
    __tablename__ = "dataset_version_lines"

    parent_uuid = Column(UUID(as_uuid=True), ForeignKey('dataset_versions.uuid', ondelete='CASCADE'), primary_key=True, nullable=False)
    child_uuid = Column(UUID(as_uuid=True), ForeignKey('dataset_versions.uuid', ondelete='CASCADE'), primary_key=True, nullable=False)

    def __repr__(self):
        return f"DatasetVersionLine(parent_uuid={self.parent_uuid!r}, child_uuid={self.child_uuid!r})"
