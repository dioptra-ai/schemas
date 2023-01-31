"""renamed datapoint.uuid top datapoint.id

Created at: 2023-01-22 19:45:38.898499
"""

revision = '3905631f8b02'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = '4871039ad30d'

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
    op.alter_column('datapoints', 'uuid', new_column_name='id')
    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('datapoints', 'id', new_column_name='uuid')
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass