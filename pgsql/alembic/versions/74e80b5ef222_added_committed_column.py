"""added committed column

Created at: 2022-08-24 18:07:19.614962
"""

revision = '74e80b5ef222'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = '9af46a66b2a8'

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
    op.add_column('events', sa.Column('committed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'committed')
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass