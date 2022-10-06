import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
POSTGRES_DATABASE = os.environ.get('POSTGRES_DATABASE', 'dioptra')

def get_session():

    return Session(
        create_engine(
            f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}",
            # Outputs all SQL queries for debugging.
            # To log queries in consumer applications instead of using this, use the following:
            # @see https://docs.sqlalchemy.org/en/14/core/engines.html#configuring-logging
            # echo=True,
            future=True,
            pool_size=1024,
            max_overflow=1024,
        )
    )
