from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, String, Boolean, CheckConstraint, text, func
from sqlalchemy.schema import Index, ForeignKey, UniqueConstraint

from .base import Base

# dataset.create()                  -> creates a new clean uncommitted version empty
# dataset.commit()                  -> commit uncommitted version
#                                   -> creates a new clean uncommitted version from committed version and create version line
#                                   -> return committed version
# dataset.checkout(uuid)            -> blocks if uncommitted version is dirty, otherwise:
#                                   -> deletes uncommitted version
#                                   -> creates a new clean uncommitted version from uuid and create version line
#                                   -> return uuid or latest committed version for 'main'
# dataset.add(...)                  -> add to uncommitted version
#                                   -> sets uncommitted version as dirty
# dataset.commit()                  -> commit uncommitted version
#                                   -> creates a new clean uncommitted version from committed version and create version line
#                                   -> return committed version
# dataset.diff(initial_uuid)        -> return diff between initial_uuid and uncommitted version
# dataset.diff('uuid_1', 'uuid_2')  -> return diff between uuid_1 and uuid_2
# dataset.rollback('uuid')          -> deletes uncommitted version
#                                   -> creates a new clean uncommitted version from uuid and create version line

class DatasetVersion(Base):
    __tablename__ = "dataset_versions"

    uuid = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    organization_id = Column(String(), nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    created_by = Column(String(), nullable=False)
    message = Column(String())
    dataset_uuid = Column(UUID(as_uuid=True), ForeignKey('datasets.uuid', ondelete='CASCADE'), nullable=False)
    dirty = Column(Boolean(), nullable=False, server_default='false')
    committed = Column(Boolean(), nullable=False, server_default='false')

    def __repr__(self):
        return f"DatasetVersion(uuid={self.uuid!r}, created_at={self.timestamp!r})"

Index('datasets_organization_id_index', DatasetVersion.organization_id)
Index('datasets_dataset_uuid_index', DatasetVersion.dataset_uuid)
# Only one uncommitted version per dataset.
Index('dataset_versions_uncomitted_unique_index', DatasetVersion.dataset_uuid, DatasetVersion.dirty, postgresql_where=DatasetVersion.committed == False, unique=True)
# No committed version can be dirty.
CheckConstraint('NOT (dirty AND committed)', name='dataset_versions_dirty_committed_exclude')
