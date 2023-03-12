"""new data model

Created at: 2023-03-01 14:10:16.381213
"""

revision = '25e1917ff79a'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = '3905631f8b02'

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
    op.execute("""DROP TYPE tasktype""")
    op.execute("""DROP TYPE featurevectortype""")
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groundtruths',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('organization_id', sa.String(), nullable=False),
    sa.Column('datapoint', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('task_type', sa.Enum('OBJECT_DETECTION', 'CLASSIFICATION', 'NER', name='tasktype'), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('class_name', sa.String(), nullable=True),
    sa.Column('top', sa.Float(), nullable=True),
    sa.Column('left', sa.Float(), nullable=True),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('width', sa.Float(), nullable=True),
    sa.ForeignKeyConstraint(['datapoint'], ['datapoints.id'], name=op.f('fk_groundtruths_datapoint_datapoints'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_groundtruths'))
    )
    op.create_index('groundtruths_organization_id_index', 'groundtruths', ['organization_id'], unique=False)
    op.create_table('predictions',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('organization_id', sa.String(), nullable=False),
    sa.Column('datapoint', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('task_type', sa.Enum('OBJECT_DETECTION', 'CLASSIFICATION', 'NER', name='tasktype'), nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('class_name', sa.String(), nullable=True),
    sa.Column('class_names', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('confidence', sa.Float(), nullable=True),
    sa.Column('confidences', postgresql.ARRAY(sa.Float()), nullable=True),
    sa.Column('top', sa.Float(), nullable=True),
    sa.Column('left', sa.Float(), nullable=True),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('width', sa.Float(), nullable=True),
    sa.Column('metrics', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('model_name', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['datapoint'], ['datapoints.id'], name=op.f('fk_predictions_datapoint_datapoints'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_predictions')),
    sa.UniqueConstraint('datapoint', 'model_name', name='predictions_datapoint_model_name_unique')
    )
    op.create_index('predictions_organization_id_index', 'predictions', ['organization_id'], unique=False)
    op.create_table('tags',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('organization_id', sa.String(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('value', sa.String(), nullable=False),
    sa.Column('datapoint', postgresql.UUID(as_uuid=True), nullable=False),
    sa.ForeignKeyConstraint(['datapoint'], ['datapoints.id'], name=op.f('fk_tags_datapoint_datapoints'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_tags')),
    sa.UniqueConstraint('datapoint', 'name', name='tags_datapoint_name_unique')
    )
    op.create_index('tags_datapoint_index', 'tags', ['datapoint'], unique=False)
    op.create_index('tags_name_index', 'tags', ['name'], unique=False)
    op.create_index('tags_organization_id_index', 'tags', ['organization_id'], unique=False)
    op.create_index('tags_value_index', 'tags', ['value'], unique=False)
    op.create_table('feature_vectors',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('organization_id', sa.String(), nullable=False),
    sa.Column('type', sa.Enum('EMBEDDINGS', 'LOGITS', name='featurevectortype'), nullable=False),
    sa.Column('datapoint', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('prediction', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('value', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('metadata', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.Column('model_name', sa.String(), nullable=True),
    sa.CheckConstraint('datapoint IS NOT NULL OR prediction IS NOT NULL', name=op.f('ck_feature_vectors_`feature_vectors_datapoint_or_prediction_set`')),
    sa.ForeignKeyConstraint(['datapoint'], ['datapoints.id'], name=op.f('fk_feature_vectors_datapoint_datapoints'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['prediction'], ['predictions.id'], name=op.f('fk_feature_vectors_prediction_predictions'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_feature_vectors')),
    sa.UniqueConstraint('datapoint', 'model_name', 'type', name='feature_vectors_datapoint_model_name_type_unique'),
    sa.UniqueConstraint('prediction', 'model_name', 'type', name='feature_vectors_prediction_model_name_type_unique')
    )
    op.create_index('feature_vector_organization_id_index', 'feature_vectors', ['organization_id'], unique=False)
    op.add_column('datapoints', sa.Column('type', sa.Enum('IMAGE', 'VIDEO', 'AUDIO', 'TEXT', name='datapointtype'), nullable=True))
    op.add_column('datapoints', sa.Column('metadata', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    op.add_column('datapoints', sa.Column('text', sa.String(), nullable=True))
    op.alter_column('datapoints', 'request_id',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('datapoints', 'request_id',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('datapoints', 'text')
    op.drop_column('datapoints', 'metadata')
    op.drop_column('datapoints', 'type')
    op.drop_index('feature_vector_organization_id_index', table_name='feature_vectors')
    op.drop_table('feature_vectors')
    op.drop_index('tags_value_index', table_name='tags')
    op.drop_index('tags_organization_id_index', table_name='tags')
    op.drop_index('tags_name_index', table_name='tags')
    op.drop_index('tags_datapoint_index', table_name='tags')
    op.drop_table('tags')
    op.drop_index('predictions_organization_id_index', table_name='predictions')
    op.drop_table('predictions')
    op.drop_index('groundtruths_organization_id_index', table_name='groundtruths')
    op.drop_table('groundtruths')
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass