import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
POSTGRES_DATABASE = os.environ.get('POSTGRES_DATABASE', 'dioptra')

engine = create_engine(
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}",
    # Outputs all SQL queries for debugging.
    # To log queries in consumer applications instead of using this, use the following:
    # @see https://docs.sqlalchemy.org/en/14/core/engines.html#configuring-logging
    # echo=True,
    future=True,
    pool_size=1024,
    max_overflow=1024,
)
# Note (Jacques - 2022/09/07)
# See https://docs.sqlalchemy.org/en/14/core/pooling.html#pooling-multiprocessing
# Doesn't seem to be working at preventing this:
# sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) SSL error: decryption failed or bad record mac
# And dince we're using werkzeug workers anyway, this is probably already in the child process anyway
# so i'm not sure if it's even useful.
engine.dispose(close=False)

def get_session():

    return Session(engine)
