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
    # Outputs all SQL queries for debugging
    # echo=True,
    future=True
)
# See https://docs.sqlalchemy.org/en/14/core/pooling.html#pooling-multiprocessing
# Doesn't seem to be working at preventing this:
# sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) SSL error: decryption failed or bad record mac
engine.dispose()

def get_session():

    return Session(engine)
