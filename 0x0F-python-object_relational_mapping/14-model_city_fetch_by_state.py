#!/usr/bin/python3
"""
    A script that prints all City objects from the database
"""


import sys
from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]))
    Base.metadata.create_all(engine)
    # Session = sessionmaker(bind=engine)
    # session = Session()
    session = sessionmaker(bind=engine)()
    for city, state in session.query(City, State).join(
            State, City.state_id == State.id).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
        # print(state.name)
        # print(city.name)
    session.close()
