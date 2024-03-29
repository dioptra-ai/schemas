"""added more columns

Created at: 2022-08-12 16:33:06.712945
"""

revision = 'a7307ab8b040'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = '45bed51232c0'

from alembic import op
import sqlalchemy as sa

from alembic import context

def upgrade():
    schema_upgrades()
    data_upgrades()

def downgrade():
    data_downgrades()
    schema_downgrades()

def schema_upgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('margin_of_confidence', sa.Float(), nullable=True))
    op.add_column('events', sa.Column('ratio_of_confidence', sa.Float(), nullable=True))
    op.add_column('events', sa.Column('original_embeddings', sa.String(), nullable=True))
    op.add_column('events', sa.Column('logits', sa.String(), nullable=True))
    op.add_column('events', sa.Column('entropy', sa.Float(), nullable=True))
    op.add_column('events', sa.Column('iou', sa.Float(), nullable=True))
    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'iou')
    op.drop_column('events', 'entropy')
    op.drop_column('events', 'logits')
    op.drop_column('events', 'original_embeddings')
    op.drop_column('events', 'ratio_of_confidence')
    op.drop_column('events', 'margin_of_confidence')
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass