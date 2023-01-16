"""removes org_id from dataset_to_datapoint

Created at: 2023-01-15 17:37:03.413556
"""

revision = '14959a2323de'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = 'e7594eea33d0'

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
    op.drop_column('dataset_to_datapoints', 'organization_id')
    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dataset_to_datapoints', sa.Column('organization_id', sa.VARCHAR(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass