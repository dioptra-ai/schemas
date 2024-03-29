"""Adding encoded mask to pred and gt

Created at: 2023-03-12 16:33:37.785297
"""

revision = '373158450074'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = '31ae1334f053'

from alembic import op
import sqlalchemy as sa
from alembic_utils.pg_grant_table import PGGrantTable
from sqlalchemy import text as sql_text
from alembic import context

def upgrade():
    schema_upgrades()
    data_upgrades()

def downgrade():
    data_downgrades()
    schema_downgrades()

def schema_upgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('groundtruths', sa.Column('encoded_segmentation_class_mask', sa.String(), nullable=True))
    op.add_column('predictions', sa.Column('encoded_segmentation_class_mask', sa.String(), nullable=True))

    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('predictions', 'encoded_segmentation_class_mask')
    op.drop_column('groundtruths', 'encoded_segmentation_class_mask')
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass