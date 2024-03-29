"""adds groundtruth unique constraint on task_type

Created at: 2023-03-26 21:12:55.243810
"""

revision = '36b6177ab6be'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = '1f15dc5cc480'

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
    op.create_unique_constraint('groundtruths_datapoint_task_type_unique', 'groundtruths', ['datapoint', 'task_type'])
    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('groundtruths_datapoint_task_type_unique', 'groundtruths', type_='unique')
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass