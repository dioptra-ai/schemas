"""adds root_parent_uuid to dataset versions

Created at: 2023-01-13 17:38:59.551271
"""

revision = 'dbb2cb27542f'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = 'c303cbabd008'

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
    op.add_column('dataset_versions', sa.Column('root_parent_uuid', postgresql.UUID(as_uuid=True), nullable=True))
    op.create_foreign_key(None, 'dataset_versions', 'dataset_versions', ['root_parent_uuid'], ['uuid'])
    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'dataset_versions', type_='foreignkey')
    op.drop_column('dataset_versions', 'root_parent_uuid')
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass