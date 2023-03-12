"""adds organization_id to dataset_to_datapoint

Created at: 2023-03-01 19:41:22.046559
"""

revision = '5716dcf95de0'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = '25e1917ff79a'

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
    op.add_column('dataset_to_datapoints', sa.Column('organization_id', sa.String(), nullable=True))
    op.create_index('dataset_to_datapoints_organization_id_index', 'dataset_to_datapoints', ['organization_id'], unique=False)

    # Populate the organization_id column based on the organization_id of the dataset_version
    op.execute("""
        UPDATE dataset_to_datapoints
        SET organization_id = dataset_versions.organization_id
        FROM dataset_versions
        WHERE dataset_to_datapoints.dataset_version = dataset_versions.uuid
    """)
    # Now make the organization_id column not nullable
    op.alter_column('dataset_to_datapoints', 'organization_id', nullable=False)

    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('dataset_to_datapoints_organization_id_index', table_name='dataset_to_datapoints')
    op.drop_column('dataset_to_datapoints', 'organization_id')
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass