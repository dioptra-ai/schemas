"""Adds on delete cascade to dataset tables

Created at: 2022-12-05 22:14:03.007101
"""

revision = 'd2e79afaf97b'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = 'b436815cd627'

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
    op.drop_constraint('dataset_to_datapoints_dataset_fkey', 'dataset_to_datapoints', type_='foreignkey')
    op.drop_constraint('dataset_to_datapoints_datapoint_fkey', 'dataset_to_datapoints', type_='foreignkey')
    op.create_foreign_key(None, 'dataset_to_datapoints', 'datasets', ['dataset'], ['uuid'], ondelete='CASCADE')
    op.create_foreign_key(None, 'dataset_to_datapoints', 'datapoints', ['datapoint'], ['uuid'], ondelete='CASCADE')
    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'dataset_to_datapoints', type_='foreignkey')
    op.drop_constraint(None, 'dataset_to_datapoints', type_='foreignkey')
    op.create_foreign_key('dataset_to_datapoints_datapoint_fkey', 'dataset_to_datapoints', 'datapoints', ['datapoint'], ['uuid'])
    op.create_foreign_key('dataset_to_datapoints_dataset_fkey', 'dataset_to_datapoints', 'datasets', ['dataset'], ['uuid'])
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass