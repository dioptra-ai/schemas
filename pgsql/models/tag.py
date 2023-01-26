from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, String, Boolean, text, func
from sqlalchemy.schema import Index, ForeignKey

from .base import Base

class Tag(Base):
    __tablename__ = "tags"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=text('gen_random_uuid()'))
    organization_id = Column(String(), nullable=False)
    name = Column(String(), nullable=False)
    value = Column(String(), nullable=False)
    datapoint = Column(UUID(as_uuid=True), ForeignKey('datapoints.id'), nullable=False)

    def __repr__(self):
        return f"Tag(id={self.id!r}, name={self.name!r}, value={self.value!r}, datapoint={self.datapoint!r})"

Index('tags_organization_id_index', Tag.organization_id)
Index('tags_datapoint_index', Tag.datapoint)
Index('tags_name_index', Tag.name)
Index('tags_value_index', Tag.value)
