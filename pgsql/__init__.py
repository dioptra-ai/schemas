import os
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_HOST = os.environ['POSTGRES_HOST']
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
POSTGRES_DATABASE = os.environ.get('POSTGRES_DATABASE', 'dioptra')

engine = create_engine(
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}", echo=True, future=True)

def get_session():

    return Session(engine)
