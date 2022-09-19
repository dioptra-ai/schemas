import datetime
import uuid
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy import Column, DateTime, String, Float, Boolean
from sqlalchemy.schema import Index

from .base import Base

class Event(Base):
    __tablename__ = "events"

    # Required, no-default fields
    organization_id = Column(String(), nullable=False)

    # Default fields
    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    timestamp = Column('timestamp', DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)
    processing_timestamp = Column(DateTime(timezone=True), nullable=False, default=datetime.datetime.utcnow)

    # Optional fields
    request_id = Column(String())
    model_id = Column(String())
    api_version = Column(String())
    model_version = Column(String())
    model_type = Column(String())
    input_type = Column(String())

    tags = Column(JSONB())
    features = Column(JSONB())
    image_metadata = Column(JSONB())
    video_metadata = Column(JSONB())
    audio_metadata = Column(JSONB())
    text_metadata = Column(JSONB())

    groundtruth = Column(JSONB())
    prediction = Column(JSONB())
    confidence = Column(Float())
    margin_of_confidence = Column(Float())
    ratio_of_confidence = Column(Float())
    embeddings = Column(String())
    original_embeddings = Column(String())
    logits = Column(String())
    entropy = Column(Float())
    iou = Column(Float())
    f1_score = Column(Float())

    dataset_id = Column(String())
    benchmark_id = Column(String())
    is_bbox_row = Column(Boolean(), default=False)

    text = Column(String())

    def __repr__(self):
        return f"Event(uuid={self.uuid!r}, timestamp={self.timestamp!r})"

Index('events_timestamp_index', Event.timestamp, postgresql_using='brin')
Index('events_organization_id_index', Event.organization_id)

# TODO: Partition by time and maybe by organization_id: https://aws.amazon.com/blogs/database/designing-high-performance-time-series-data-tables-on-amazon-rds-for-postgresql/
