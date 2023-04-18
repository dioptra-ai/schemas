"""adds metrics column to groundtruth

Created at: 2023-03-16 20:26:02.788285
"""

revision = '1e03385079d4'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = 'f0c2f11154d4'

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
    op.add_column('groundtruths', sa.Column('metrics', postgresql.JSONB(astext_type=sa.Text()), nullable=True))
    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('groundtruths', 'metrics')
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass