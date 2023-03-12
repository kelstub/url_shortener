from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import get_settings

#Engine is the entry point to the database
engine = create_engine(
    get_settings().db_url, connect_args={"check_same_thread": False}
    # check_same_threas is set to false because I'm working with an SQLite db
)
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)
# declariative_base returns a class that connectes the database engine to
# the SQLAlchemy functionality of the models.
Base = declarative_base()