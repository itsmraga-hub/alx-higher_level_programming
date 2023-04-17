#!/usr/bin/python3
"""
    A script that prints the State object with the name
    passed as argument fromthe database
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import State, Base

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name == sys.argv[4])
    state = states.first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
