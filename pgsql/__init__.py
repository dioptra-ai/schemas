import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
POSTGRES_DATABASE = os.environ.get('POSTGRES_DATABASE', 'dioptra')
POSTGRES_MAX_CONNECTIONS = int(os.environ.get('POSTGRES_MAX_CONNECTIONS', 2048))

def get_session():

    return Session(
        create_engine(
            f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}",
            # echo=True,
            future=True,
            pool_size=POSTGRES_MAX_CONNECTIONS / 2,
            max_overflow=POSTGRES_MAX_CONNECTIONS / 2,
        )
    )

def run_sql_query(sql_query):
    engine = create_engine(
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}",
        # echo=True,
        future=True,
        pool_size=POSTGRES_MAX_CONNECTIONS / 2,
        max_overflow=POSTGRES_MAX_CONNECTIONS / 2,
    )

    with engine.connect() as conn:
        return conn.execute(text(sql_query))
