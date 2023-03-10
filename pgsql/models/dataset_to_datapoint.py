from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, String, func
from sqlalchemy.schema import ForeignKey, Index

from .base import Base

class DatasetToDatapoint(Base):
    __tablename__ = 'dataset_to_datapoints'

    dataset_version = Column(UUID(as_uuid=True), ForeignKey('dataset_versions.uuid', ondelete='CASCADE'), primary_key=True, nullable=False)
    datapoint = Column(UUID(as_uuid=True), ForeignKey('datapoints.id', ondelete='CASCADE'), primary_key=True, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    organization_id = Column(String(), nullable=False)

    def __repr__(self):
        return f'DatasetToDatapoint(organization_id={self.organization_id!r}, dataset_version={self.dataset_version!r}, datapoint={self.datapoint!r}, created_at={self.created_at!r})'

Index('dataset_to_datapoints_organization_id_index', DatasetToDatapoint.organization_id)
