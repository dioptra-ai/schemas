"""adds bbox table for instance segmentation

Created at: 2023-04-13 17:14:32.843841
"""

revision = 'bf2904dc3cef'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = '68301370c478'

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
    op.create_table('bboxes',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('gen_random_uuid()'), nullable=False),
    sa.Column('organization_id', sa.String(), nullable=False),
    sa.Column('prediction', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('groundtruth', postgresql.UUID(as_uuid=True), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('class_name', sa.String(), nullable=True),
    sa.Column('class_names', postgresql.ARRAY(sa.String()), nullable=True),
    sa.Column('confidence', sa.Float(), nullable=True),
    sa.Column('confidences', postgresql.ARRAY(sa.Float()), nullable=True),
    sa.Column('encoded_resized_segmentation_mask', sa.String(), nullable=True),
    sa.Column('encoded_segmentation_mask', sa.String(), nullable=True),
    sa.Column('top', sa.Float(), nullable=True),
    sa.Column('left', sa.Float(), nullable=True),
    sa.Column('height', sa.Float(), nullable=True),
    sa.Column('width', sa.Float(), nullable=True),
    sa.Column('metrics', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
    sa.ForeignKeyConstraint(['groundtruth'], ['groundtruths.id'], name=op.f('fk_bboxes_groundtruth_groundtruths'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['prediction'], ['predictions.id'], name=op.f('fk_bboxes_prediction_predictions'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_bboxes'))
    )
    op.create_index('bboxes_class_name_index', 'bboxes', ['class_name'], unique=False)
    op.create_index('bboxes_confidence_index', 'bboxes', ['confidence'], unique=False)
    op.create_index('bboxes_groundtruth_index', 'bboxes', ['groundtruth'], unique=False)
    op.create_index('bboxes_organization_id_index', 'bboxes', ['organization_id'], unique=False)
    op.create_index('bboxes_prediction_index', 'bboxes', ['prediction'], unique=False)
    op.add_column('feature_vectors', sa.Column('bbox', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_index('feature_vector_bbox_index', 'feature_vectors', ['bbox'], unique=False)
    op.create_unique_constraint('feature_vectors_bbox_model_name_type_unique', 'feature_vectors', ['bbox', 'model_name', 'type'])
    op.create_foreign_key(op.f('fk_feature_vectors_bbox_bboxes'), 'feature_vectors', 'bboxes', ['bbox'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###

    # Rename tasktype enum value SEGMENTATION to SEMANTIC_SEGMENTATION
    op.execute("ALTER TYPE tasktype RENAME VALUE 'SEGMENTATION' TO 'SEMANTIC_SEGMENTATION'")
    # Add new tasktype enum value INSTANCE_SEGMENTATION
    op.execute("ALTER TYPE tasktype ADD VALUE IF NOT EXISTS 'INSTANCE_SEGMENTATION'")


def schema_downgrades():
    # Revert the tasktype migration above
    op.execute("ALTER TYPE tasktype RENAME VALUE 'SEMANTIC_SEGMENTATION' TO 'SEGMENTATION'")    

    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_feature_vectors_bbox_bboxes'), 'feature_vectors', type_='foreignkey')
    op.drop_constraint('feature_vectors_bbox_model_name_type_unique', 'feature_vectors', type_='unique')
    op.drop_index('feature_vector_bbox_index', table_name='feature_vectors')
    op.drop_column('feature_vectors', 'bbox')
    op.drop_index('bboxes_prediction_index', table_name='bboxes')
    op.drop_index('bboxes_organization_id_index', table_name='bboxes')
    op.drop_index('bboxes_groundtruth_index', table_name='bboxes')
    op.drop_index('bboxes_confidence_index', table_name='bboxes')
    op.drop_index('bboxes_class_name_index', table_name='bboxes')
    op.drop_table('bboxes')
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass