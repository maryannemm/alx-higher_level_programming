#!/usr/bin/python3
"""Define State class and Base instance."""
import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    """State class."""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database_name>".format(sys.argv[0]))
        sys.exit(1)
    
    username, password, database_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/'
                           .format(username, password), pool_pre_ping=True)

    # Create database if not exists
    with engine.connect() as connection:
        connection.execute("CREATE DATABASE IF NOT EXISTS {}".format(database_name))
        connection.execute("USE {}".format(database_name))

    # Create all tables in the engine
    Base.metadata.create_all(engine)

