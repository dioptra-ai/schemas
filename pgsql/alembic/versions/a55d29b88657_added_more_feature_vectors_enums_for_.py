"""added more feature vectors enums for pixel entropy and variance

Created at: 2023-03-25 15:37:12.603128
"""

revision = 'a55d29b88657'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = 'b20dd50cf6f8'

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

####
#
# Manually generated based on
# https://makimo.pl/blog/upgrading-postgresqls-enum-type-with-sqlalchemy-using-alembic-migration/
#
####
def schema_upgrades():
    with op.get_context().autocommit_block():
        op.execute("ALTER TYPE featurevectortype ADD VALUE 'PXL_ENTROPY'")
        op.execute("ALTER TYPE featurevectortype ADD VALUE 'PXL_VARIANCE'")

def schema_downgrades():
    op.execute("ALTER TYPE featurevectortype RENAME TO featurevectortype_old")
    op.execute("CREATE TYPE featurevectortype AS ENUM('EMBEDDINGS', 'LOGITS')")
    op.execute((
        "ALTER TABLE feature_vectors ALTER COLUMN type TYPE featurevectortype USING "
        "type::text::featurevectortype"
    ))
    op.execute("DROP TYPE featurevectortype_old")

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass