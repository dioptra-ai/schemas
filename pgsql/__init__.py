import os
from sqlalchemy import create_engine, text, event, exc
from sqlalchemy.orm import Session
import json

ENVIRONMENT = os.environ.get('ENVIRONMENT', 'dev')
POSTGRES_DATABASE = os.environ.get('POSTGRES_DATABASE', 'dioptra')
POSTGRES_MAX_CONNECTIONS = int(os.environ.get('POSTGRES_MAX_CONNECTIONS', 2048))
POSTGRES_ECHO = os.environ.get('POSTGRES_ECHO', 'false') == 'true'

if POSTGRES_ECHO:
    import logging
    logging.basicConfig()
    logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# If this pops up in production sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) SSL SYSCALL error: EOF detected
# try this: https://www.roelpeters.be/error-ssl-syscall-error-eof-detected/

import boto3
def aws_get_from_secret_manager(secret_name, region_name = 'us-east-2'):

    secret_json = boto3.session.Session().client(
        service_name='secretsmanager',
        region_name=region_name
    ).get_secret_value(SecretId=secret_name)['SecretString']

    return json.loads(secret_json)

try:
    postgres_credentials = aws_get_from_secret_manager(f'{ENVIRONMENT}/postgres-credentials')

    POSTGRES_USER = postgres_credentials['username']
    POSTGRES_PASSWORD = postgres_credentials['password']
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST', postgres_credentials['host'])
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', postgres_credentials['port'])
except Exception as e:
    print(f'WARNING: Failed to get postgres credentials from AWS Secrets Manager: {e}. Falling back to environment variables...')
    POSTGRES_USER = os.environ['POSTGRES_USER']
    POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
    POSTGRES_HOST = os.environ['POSTGRES_HOST']
    POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
else:
    print('Successfully got postgres credentials from AWS Secrets Manager')

_sql_engine = create_engine(
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}",
    future=True,
    pool_size=POSTGRES_MAX_CONNECTIONS / 2,
    max_overflow=POSTGRES_MAX_CONNECTIONS / 2,
)

@event.listens_for(_sql_engine, "connect")
def connect(dbapi_connection, connection_record):
    connection_record.info["pid"] = os.getpid()

@event.listens_for(_sql_engine, "checkout")
def checkout(dbapi_connection, connection_record, connection_proxy):
    pid = os.getpid()
    if connection_record.info["pid"] != pid:
        connection_record.dbapi_connection = connection_proxy.dbapi_connection = None
        raise exc.DisconnectionError(
            "Connection record belongs to pid %s, "
            "attempting to check out in pid %s" % (connection_record.info["pid"], pid)
        )

def get_sql_engine():

    return _sql_engine

def new_sql_engine(host, port):

    return create_engine(
        f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{host}:{port}/{POSTGRES_DATABASE}",
        future=True,
        pool_size=POSTGRES_MAX_CONNECTIONS / 2,
        max_overflow=POSTGRES_MAX_CONNECTIONS / 2,
    )

def get_session():

    return Session(get_sql_engine())

def run_sql_query(sql_query, commit=False, engine=_sql_engine):

    with engine.connect() as conn:
        result = conn.execute(text(sql_query))

        if commit:
            conn.commit()
        
        return result
