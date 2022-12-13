import os
from sqlalchemy import create_engine, text, event, exc
from sqlalchemy.orm import Session

POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
POSTGRES_DATABASE = os.environ.get('POSTGRES_DATABASE', 'dioptra')
POSTGRES_MAX_CONNECTIONS = int(os.environ.get('POSTGRES_MAX_CONNECTIONS', 2048))
POSTGRES_ECHO = os.environ.get('POSTGRES_ECHO', 'false') == 'true'

# If this pops up in production sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) SSL SYSCALL error: EOF detected
# try this: https://www.roelpeters.be/error-ssl-syscall-error-eof-detected/

_sql_engine = create_engine(
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DATABASE}",
    echo=POSTGRES_ECHO,
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

def get_session():

    return Session(get_sql_engine())

def run_sql_query(sql_query):

    with get_sql_engine().connect() as conn:
        return conn.execute(text(sql_query))
