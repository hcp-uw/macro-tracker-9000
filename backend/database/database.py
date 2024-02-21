from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

load_dotenv()

host = os.getenv("DATABASE_HOST")
user = os.getenv("DATABASE_USERNAME")
passwd = os.getenv("DATABASE_PASSWORD")
db = os.getenv("DATABASE")

SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{user}:{passwd}@{host}/{db}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

Base = declarative_base()

# Load environment variables from the .env file
# import os
# import MySQLdb

# # Connect to the database
# connection = MySQLdb.connect(
#   host=os.getenv("DATABASE_HOST"),
#   user=os.getenv("DATABASE_USERNAME"),
#   passwd=os.getenv("DATABASE_PASSWORD"),
#   db=os.getenv("DATABASE"),
#   autocommit=True,
#   ssl_mode="VERIFY_IDENTITY",
#   # See https://planetscale.com/docs/concepts/secure-connections#ca-root-configuration
#   # to determine the path to your operating systems certificate file.
#   ssl={ "ca": "" }
# )