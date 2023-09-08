# # the schema of the tables will be in this file


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base =declarative_base()


class Recipe(Base):
    __tablename__="recipes"

    id= Column(Integer, primary_key=True)
    name =Column (String())
    description= Column(String())



    def __repr__(self):
        return f"Recipe(id={self.id!r}, name={self.name!r}, description={self.description!r})"
    ingredients = relationship('RecipeIngredient', back_populates='recipe')
    # categories = relationship('RecipeCategory', back_populates='recipe')
    categories = relationship('RecipeCategory', back_populates='recipe', cascade='all, delete-orphan')
    recipe_ingredients = relationship("RecipeIngredient", back_populates="recipe", overlaps="ingredients")

class Ingredient(Base):
    __tablename__='ingredients'

    id= Column(Integer, primary_key=True)
    name= Column(String)
    quantity= Column(String, nullable=True)
    units= Column(String, nullable=True)
    recipeId= Column(Integer , ForeignKey('recipes.id'))

    recipes = relationship('RecipeIngredient', back_populates='ingredient')

    def __repr__(self):
        return f"Ingredient(id={self.id!r}, name={self.name}, recipeId={self.recipeId})"


class Category(Base):
    __tablename__='foodcategories'

    id= Column(Integer, primary_key=True)
    name= Column(String)
    recipeId= Column(Integer , ForeignKey('recipes.id'))

    # recipes = relationship('RecipeCategory', back_populates='category')
    recipes = relationship('RecipeCategory', back_populates='category', cascade='all, delete-orphan')
    def __repr__(self):
        return f"Category(id={self.id!r}, name={self.name}, recipeId={self.recipeId})"
    


# join tables

class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredient'


    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True)
    quantity = Column(String)
    units = Column(String)


    recipe = relationship('Recipe', back_populates='ingredients')
    ingredient = relationship('Ingredient', back_populates='recipes')

    def __repr__(self):
        return f"RecipeIngredient(id={self.id!r}, recipe_id={self.recipe_id!r}, ingredient_id={self.ingredient_id!r}, quantity={self.quantity!r}, units={self.units!r})"
    

class RecipeCategory(Base):
    __tablename__ = 'recipe_category'

     
    recipe_id = Column(Integer, ForeignKey('recipes.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('foodcategories.id'), primary_key=True)




    recipe = relationship('Recipe', back_populates='categories')
    category = relationship('Category', back_populates='recipes')

    def __repr__(self):
        return f"RecipeCategory(id={self.id!r}, recipe_id={self.recipe_id!r}, category_id={self.category_id!r})"



