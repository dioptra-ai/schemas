"""Adds index to model_id

Created at: 2022-10-02 23:10:36.490379
"""

revision = '8e1abb32f0d9'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = '288f7f9295ef'

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
    op.create_index('events_dataset_id_index', 'events', ['dataset_id'], unique=False)
    op.create_index('events_model_id_index', 'events', ['model_id'], unique=False)
    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('events_model_id_index', table_name='events')
    op.drop_index('events_dataset_id_index', table_name='events')
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass