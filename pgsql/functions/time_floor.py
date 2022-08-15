from alembic_utils.pg_function import PGFunction

time_floor = PGFunction(
    schema='public',
    signature='TIME_FLOOR(t timestamp with time zone, i interval)',
    definition="""
        RETURNS timestamp with time zone AS 
        $$
        BEGIN
            RETURN date_bin(i, t, timestamptz '1970-01-01T00:00:00.000Z');
        END; 
        $$ LANGUAGE plpgsql;
    """
)
