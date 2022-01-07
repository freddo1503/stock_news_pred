import os
import sqlalchemy

# Hydrate the environment from the .env file
from dotenv import load_dotenv
load_dotenv()

def init_db_connection():
    db_config = {
        'pool_size': 5,
        'max_overflow': 2,
        'pool_timeout': 30,
        'pool_recycle': 1800,
    }
    return init_unix_connection_engine(db_config)

def init_unix_connection_engine(db_config):
    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASS'),
            database=os.environ.get('DB_NAME'),
            query={
                "unix_socket": "/cloudsql/{}".format(
                os.environ.get('CLOUD_SQL_CONNECTION_NAME'))  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
        }
        ),
        **db_config
    )
    pool.dialect.description_encoding = None
    return pool
    