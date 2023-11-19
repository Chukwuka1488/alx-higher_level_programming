#!/usr/bin/python3
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """State class to map the 'states' table in the database."""

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)

    def __repr__(self):
        """Representation of the State object."""
        return f"<State(id={self.id}, name={self.name})>"


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Retrieve arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Establish database connection using SQLAlchemy
    engine = create_engine(
        f"mysql://{username}:{password}@localhost:3306/{database}")
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Query to retrieve states sorted by id using ORM
        states = session.query(State).order_by(State.id).all()

        # Display results
        for state in states:
            print((state.id, state.name))

    except Exception as e:
        print("Error:", e)
        sys.exit(1)

    finally:
        # Close the session
        session.close()
