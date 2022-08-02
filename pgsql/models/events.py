import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime

from .base import Base

class Event(Base):
    __tablename__ = "events"
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    __time = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f"Event(uuid={self.uuid}, __time={self.__time})"
