#!/usr/bin/python3
"""a script that lists all State objects from the database hbtn_0e_6_usa"""

if __name__ == "__main__":
    import sys
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sqlalchemy import create_engine

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        mysql_username, mysql_password, database_name), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")