
# establishing and creating the db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.model import Base

DATABASE_URL = 'sqlite:///ourrecipes.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()
