# initializing and creating our database


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.model import Base
engine= create_engine('sqlite:///ourrecipes.db')

# creating all the tables

# creating session to interact with the db
Session = sessionmaker(bind=engine)
session= Session()

Base.metadata.create_all(engine)


session.commit()
session.close()


#schema for my tables





