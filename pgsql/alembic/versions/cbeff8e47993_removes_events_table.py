"""removes events table

Created at: 2023-06-16 16:04:41.071758
"""

revision = 'cbeff8e47993'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = '4d0e57a9565d'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql
from alembic import context

def upgrade():
    schema_upgrades()
    data_upgrades()

def downgrade():
    data_downgrades()
    schema_downgrades()

def schema_upgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('events_dataset_id_index', table_name='events')
    op.drop_index('events_features_index', table_name='events')
    op.drop_index('events_model_id_index', table_name='events')
    op.drop_index('events_organization_id_index', table_name='events')
    op.drop_index('events_request_id_index', table_name='events')
    op.drop_index('events_tags_index', table_name='events')
    op.drop_index('events_timestamp_index', table_name='events')
    op.drop_table('events')
    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('uuid', postgresql.UUID(), autoincrement=False, nullable=False),
    sa.Column('timestamp', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('request_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('organization_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('processing_timestamp', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('model_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('api_version', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('model_version', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('model_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('input_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('features', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('image_metadata', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('video_metadata', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('audio_metadata', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('text_metadata', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('groundtruth', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('prediction', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('confidence', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('embeddings', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('tags', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.Column('dataset_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('is_bbox_row', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('benchmark_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('text', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('margin_of_confidence', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('ratio_of_confidence', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('original_embeddings', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('logits', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('entropy', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('iou', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('f1_score', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('metrics', postgresql.JSONB(astext_type=sa.Text()), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('uuid', name='pk_events')
    )
    op.create_index('events_timestamp_index', 'events', ['timestamp'], unique=False)
    op.create_index('events_tags_index', 'events', ['tags'], unique=False)
    op.create_index('events_request_id_index', 'events', ['request_id'], unique=False)
    op.create_index('events_organization_id_index', 'events', ['organization_id'], unique=False)
    op.create_index('events_model_id_index', 'events', ['model_id'], unique=False)
    op.create_index('events_features_index', 'events', ['features'], unique=False)
    op.create_index('events_dataset_id_index', 'events', ['dataset_id'], unique=False)
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass