# the schema of the tables will be in this file


from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base =declarative_base()


# defining the joint tables
recipe_category = Table(
    'recipe_category',
    Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.id')),
    Column('category_id', Integer, ForeignKey('foodcategories.id'))
)

recipe_ingredient = Table(
    'recipe_ingredient',
    Base.metadata,
    Column('recipe_id', Integer, ForeignKey('recipes.id')),
    Column('ingredient_id', Integer, ForeignKey('ingredients.id'))
)

class Recipe(Base):
    __tablename__="recipes"

    id= Column(Integer, primary_key=True)
    name =Column (String())
    description= Column(String)
    cooking_time = Column(Integer)  



    def __repr__(self):
        return f"Recipe(id={self.id!r}, name={self.name!r}, description={self.description!r})"
    categories = relationship('Category', secondary='recipe_category', back_populates='recipes')
    ingredients = relationship('Ingredient', secondary='recipe_ingredient', back_populates='recipes')


class Ingredient(Base):
    __tablename__='ingredients'

    id= Column(Integer, primary_key=True)
    name= Column(String)
    quantity= Column(String)
    units= Column(String)
    recipeId= Column(Integer , ForeignKey('recipes.id'))

    recipes = relationship('Recipe', secondary='recipe_ingredient', back_populates='ingredients')


    def __repr__(self):
        return f"Ingredient(id={self.id!r}, name={self.name}, recipeId={self.recipeId})"


class Category(Base):
    __tablename__='foodcategories'

    id= Column(Integer, primary_key=True)
    name= Column(String)
    recipeId= Column(Integer , ForeignKey('recipes.id'))

    recipes = relationship('Recipe', secondary='recipe_category', back_populates='categories')

    def __repr__(self):
        return f"Category(id={self.id!r}, name={self.name}, recipeId={self.recipeId})"
    


# join tables

# class RecipeIngredient(Base):
#     __tablename__ = 'recipe_ingredient'

#     id = Column(Integer, primary_key=True)
#     recipe_id = Column(Integer, ForeignKey('recipes.id'))
#     ingredient_id = Column(Integer, ForeignKey('ingredients.id'))
#     quantity = Column(String)
#     units = Column(String)

#     recipe = relationship('Recipe', back_populates='ingredients')
#     ingredient = relationship('Ingredient', back_populates='recipes')

#     def __repr__(self):
#         return f"RecipeIngredient(id={self.id!r}, recipe_id={self.recipe_id!r}, ingredient_id={self.ingredient_id!r}, quantity={self.quantity!r}, units={self.units!r})"
    


# class RecipeCategory(Base):
#     __tablename__ = 'recipe_category'

#     id = Column(Integer, primary_key=True)
#     recipe_id = Column(Integer, ForeignKey('recipes.id'))
#     category_id = Column(Integer, ForeignKey('foodcategories.id'))

#     recipe = relationship('Recipe', back_populates='categories')
#     category = relationship('Category', back_populates='recipes')

#     def __repr__(self):
#         return f"RecipeCategory(id={self.id!r}, recipe_id={self.recipe_id!r}, category_id={self.category_id!r})"



