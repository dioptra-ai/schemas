"""adds indexes on all datapoint foreign keys

Created at: 2023-03-21 14:44:58.323918
"""

revision = '64c8cde6c4c8'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = '1e03385079d4'

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
    op.create_index('dataset_to_datapoints_dataset_version_index', 'dataset_to_datapoints', ['dataset_version'], unique=False)
    op.create_index('dataset_to_datapoints_datpoint_index', 'dataset_to_datapoints', ['datapoint'], unique=False)
    op.create_index('dataset_version_lines_child_uuid_index', 'dataset_version_lines', ['child_uuid'], unique=False)
    op.create_index('dataset_version_lines_parent_uuid_index', 'dataset_version_lines', ['parent_uuid'], unique=False)
    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('dataset_version_lines_parent_uuid_index', table_name='dataset_version_lines')
    op.drop_index('dataset_version_lines_child_uuid_index', table_name='dataset_version_lines')
    op.drop_index('dataset_to_datapoints_datpoint_index', table_name='dataset_to_datapoints')
    op.drop_index('dataset_to_datapoints_dataset_version_index', table_name='dataset_to_datapoints')
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass