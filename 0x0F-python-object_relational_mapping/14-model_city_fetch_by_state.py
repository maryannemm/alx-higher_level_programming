#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    # Create a connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all City objects and join them with their corresponding State objects
    cities = session.query(City, State).filter(City.state_id == State.id).order_by(City.id).all()

    # Print the results
    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

