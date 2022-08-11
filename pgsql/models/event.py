import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import synonym
from sqlalchemy import Column, DateTime, String, Float

from .base import Base

class Event(Base):
    __tablename__ = "events"

    # Required, no-default fields
    organization_id = Column(String(), nullable=False)

    # Default fields
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    __time = Column('__time', DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    timestamp = synonym('__time')
    processing_timestamp = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)

    # Optional fields
    request_id = Column(String())
    model_id = Column(String())
    api_version = Column(String())
    model_version = Column(String())
    model_type = Column(String())
    input_type = Column(String())

    tags = Column('tags', JSONB())
    features = Column(JSONB())
    image_metadata = Column(JSONB())
    video_metadata = Column(JSONB())
    audio_metadata = Column(JSONB())
    text_metadata = Column(JSONB())

    groundtruth = Column(JSONB())
    prediction = Column(JSONB())
    confidence = Column(Float())
    embeddings = Column(String())

    def __repr__(self):
        return f"Event(uuid={self.uuid!r}, __time={self.__time!r})"
