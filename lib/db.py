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
    # quantity= Column(String)
    # units= Column(String)
    recipeId= Column(Integer , ForeignKey('recipes.id'))

    def __repr__(self):
        return f"Ingredient(id={self.id!r}, name={self.name}, recipeId={self.recipeId})"
    

class StepTable(Base):
    __tablename__='stepstofollow'

    id= Column(Integer, primary_key=True)
    description= Column(String)
    # steporder= Column(Integer)
    recipeId= Column(Integer , ForeignKey('recipes.id'))

    def __repr__(self):
        return f"StepTable(id={self.id!r}, description={self.description}, recipeId={self.recipeId})"
    

class Category(Base):
    __tablename__='foodcategories'

    id= Column(Integer, primary_key=True)
    name= Column(String)
    recipeId= Column(Integer , ForeignKey('recipes.id'))

    def __repr__(self):
        return f"Category(id={self.id!r}, name={self.name}, recipeId={self.recipeId})"
    

# join tables

class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredient'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
    quantity = Column(String)
    units = Column(String)

    recipe = relationship('Recipe', back_populates='ingredients')
    ingredient = relationship('Ingredient', back_populates='recipes')

    def __repr__(self):
        return f"RecipeIngredient(id={self.id!r}, recipe_id={self.recipe_id!r}, ingredient_id={self.ingredient_id!r}, quantity={self.quantity!r}, units={self.units!r})"
    
class RecipeStep(Base):
    __tablename__ = 'recipe_step'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    step_id = Column(Integer, ForeignKey('stepstofollow.id'))
    step_order = Column(Integer)

    recipe = relationship('Recipe', back_populates='steps')
    step = relationship('StepTable', back_populates='recipes')

    def __repr__(self):
        return f"RecipeStep(id={self.id!r}, recipe_id={self.recipe_id!r}, step_id={self.step_id!r}, step_order={self.step_order!r})"
    


class RecipeCategory(Base):
    __tablename__ = 'recipe_category'

    id = Column(Integer, primary_key=True)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    category_id = Column(Integer, ForeignKey('foodcategories.id'))

    recipe = relationship('Recipe', back_populates='categories')
    category = relationship('Category', back_populates='recipes')

    def __repr__(self):
        return f"RecipeCategory(id={self.id!r}, recipe_id={self.recipe_id!r}, category_id={self.category_id!r})"







