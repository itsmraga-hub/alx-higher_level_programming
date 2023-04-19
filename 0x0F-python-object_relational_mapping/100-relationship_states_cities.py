#!/usr/bin/python3
"""
    A script that creates the `State` California with
    the city San Francisco
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    # city = City(name="San Francisco")
    state = State(name="California")
    city = City(name="San Francisco")
    state.cities.append(city)
    print(state)
    session.add(state)
    session.add(city)
    session.commit()
    session.close()
