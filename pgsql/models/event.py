import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, String

from .base import Base

class Event(Base):
    __tablename__ = "events"

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    __time = Column('__time', DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    request_id = Column(String())
    organization_id = Column(String(), nullable=False)

    def __repr__(self):
        return f"Event(uuid={self.uuid!r}, __time={self.__time!r})"
