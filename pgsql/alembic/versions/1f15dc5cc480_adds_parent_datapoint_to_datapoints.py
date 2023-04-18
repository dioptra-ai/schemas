"""adds parent_datapoint to datapoints

Created at: 2023-03-26 18:11:37.499252
"""

revision = '1f15dc5cc480'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = 'b7d7d3395e89'

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
    op.add_column('datapoints', sa.Column('parent_datapoint', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_index('datapoints_parent_datapoint_index', 'datapoints', ['parent_datapoint'], unique=False)
    op.create_foreign_key(op.f('fk_datapoints_parent_datapoint_datapoints'), 'datapoints', 'datapoints', ['parent_datapoint'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_datapoints_parent_datapoint_datapoints'), 'datapoints', type_='foreignkey')
    op.drop_index('datapoints_parent_datapoint_index', table_name='datapoints')
    op.drop_column('datapoints', 'parent_datapoint')
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass