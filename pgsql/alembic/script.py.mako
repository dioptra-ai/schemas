"""${message}

Created at: ${create_date}
"""

revision = ${repr(up_revision)}
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = ${repr(down_revision)}

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}
from alembic import context

def upgrade():
    schema_upgrades()
    data_upgrades()

def downgrade():
    data_downgrades()
    schema_downgrades()

def schema_upgrades():
    ${upgrades if upgrades else "pass"}

def schema_downgrades():
    ${downgrades if downgrades else "pass"}

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass