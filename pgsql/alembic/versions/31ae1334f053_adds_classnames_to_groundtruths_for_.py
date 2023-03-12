"""adds classnames to groundtruths for segmentation use-case

Created at: 2023-03-09 16:20:29.417660
"""

revision = '31ae1334f053'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = 'fa14c4bb73bc'

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
    op.add_column('groundtruths', sa.Column('class_names', postgresql.ARRAY(sa.String()), nullable=True))
    op.drop_column('predictions', 'variances')
    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('predictions', sa.Column('variances', postgresql.ARRAY(postgresql.DOUBLE_PRECISION(precision=53)), autoincrement=False, nullable=True))
    op.drop_column('groundtruths', 'class_names')
    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass