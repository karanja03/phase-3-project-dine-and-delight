from sqlalchemy import Column, Integer, String, ForeignKey
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
    

class Ingredient(Base):
    __tablename__='ingredients'

    id= Column(Integer, primary_key=True)
    name= Column(String)
    quantity= Column(String)
    units= Column(String)
    recipeId= Column(Integer , ForeignKey('recipes.id'))

    def __repr__(self):
        return f"Ingredient(id={self.id!r}, name={self.name}, quantity={self.quantity}, units= {self.units}, recipeId={self.recipeId})"
    

class StepTable(Base):
    __tablename__='stepstofollow'

    id= Column(Integer, primary_key=True)
    description= Column(String)
    steporder= Column(Integer)
    recipeId= Column(Integer , ForeignKey('recipes.id'))

    def __repr__(self):
        return f"StepTable(id={self.id!r}, description={self.description},  steporder= {self.steporder}, recipeId={self.recipeId})"
    

class Category(Base):
    __tablename__='foodcategories'

    id= Column(Integer, primary_key=True)
    name= Column(String)
    recipeId= Column(Integer , ForeignKey('recipes.id'))

    def __repr__(self):
        return f"Category(id={self.id!r}, name={self.name}, recipeId={self.recipeId})"


