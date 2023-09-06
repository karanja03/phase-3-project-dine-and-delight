from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship


Base= declarative_base()


#schema for my tables

class Recipe(Base):
    __tablename__="recipes"

    id= Column(Integer, primary_key=True)
    name =Column (String())
    description= Column(String)


    def __repr__(self):
        return f"Recipe(id={self.id!r}, name={self.name!r}, description={self.description!r})"
    

class 
