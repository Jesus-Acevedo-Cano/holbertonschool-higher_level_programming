#!/usr/bin/python3
"""script that lists all State objects from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
"""modules import"""

if __name__ == '__main__':
    """arguments order"""
    user = sys.argv[1]
    pswrd = sys.argv[2]
    db = sys.argv[3]
    search = sys.argv[4]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, pswrd, db),
        pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).filter_by(name=search).order_by(State.id).all()
    if not res:
        print("Not found")
    for row in res:
        print("{}".format(row.id))
    session.close()
