"""added SQL time_floor lowercase...

Created at: 2022-08-22 14:08:00.474021
"""

revision = '9af46a66b2a8'
# To prune migrations prior to this one, set this down_revision to None
# and delete the files of the prior revisions.
down_revision = '08c569b0772c'

from alembic import op
import sqlalchemy as sa
from alembic_utils.pg_function import PGFunction
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
    public_time_floor = PGFunction(
        schema="public",
        signature="time_floor(t timestamp with time zone, i interval)",
        definition="RETURNS timestamp with time zone AS \n        $$\n        BEGIN\n            RETURN date_bin(i, t, timestamptz '1970-01-01T00:00:00.000Z');\n        END; \n        $$ LANGUAGE plpgsql"
    )
    op.create_entity(public_time_floor)

    public_time_floor = PGFunction(
        schema="public",
        signature="TIME_FLOOR(t timestamp with time zone, i interval)",
        definition="returns timestamp with time zone\n LANGUAGE sql\nAS $function$\n      SELECT date_bin(i, t, timestamptz '1970-01-01T00:00:00.000Z');\n    $function$"
    )
    op.drop_entity(public_time_floor)

    # ### end Alembic commands ###

def schema_downgrades():
    # ### commands auto generated by Alembic - please adjust! ###
    public_time_floor = PGFunction(
        schema="public",
        signature="TIME_FLOOR(t timestamp with time zone, i interval)",
        definition="returns timestamp with time zone\n LANGUAGE sql\nAS $function$\n      SELECT date_bin(i, t, timestamptz '1970-01-01T00:00:00.000Z');\n    $function$"
    )
    op.create_entity(public_time_floor)

    public_time_floor = PGFunction(
        schema="public",
        signature="time_floor(t timestamp with time zone, i interval)",
        definition="RETURNS timestamp with time zone AS \n        $$\n        BEGIN\n            RETURN date_bin(i, t, timestamptz '1970-01-01T00:00:00.000Z');\n        END; \n        $$ LANGUAGE plpgsql"
    )
    op.drop_entity(public_time_floor)

    # ### end Alembic commands ###

def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass

def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass