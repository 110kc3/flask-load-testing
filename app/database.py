from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
import os
import sqlalchemy

#load secrets from environment variables
db_user = os.environ["CLOUD_SQL_USERNAME"]
db_pass = os.environ["CLOUD_SQL_PASSWORD"]
db_name = os.environ["CLOUD_SQL_DATABASE_NAME"]
db_host = os.environ["CLOUD_SQL_CONNECTION_NAME"]

# Extract port from db_host if present,
# otherwise use DB_PORT environment variable.
# host_args = db_host.split(":")
# if len(host_args) == 1:
#     db_hostname = db_host
#     db_port = os.environ["DB_PORT"]
# elif len(host_args) == 2:
#     db_hostname, db_port = host_args[0], int(host_args[1])


db_hostname = "127.0.0.1" # Use localhost as cloud-sql-proxy is in the same pod  - db ip: 34.118.93.58
db_port = "3306"
pool = sqlalchemy.create_engine(
    # Equivalent URL:
    # mysql+mysqldb://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
    sqlalchemy.engine.url.URL.create(
        drivername="mysql+pymysql",
        username=db_user,  # e.g. "my-database-user"
        password=db_pass,  # e.g. "my-database-password"
        host=db_hostname,  # e.g. "127.0.0.1"
        port=db_port,  # e.g. 3306
        database=db_name,  # e.g. "my-database-name"
    )
    # **db_config
)

Session = sessionmaker(bind=pool)
session = Session()