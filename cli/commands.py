#  all the logic and commands for cli will go in here

import click
from database.model import Recipe, Ingredient, Category, RecipeIngredient, RecipeCategory
from database.db import session

@click.group()

def main():
    """WELCOME TO DIne AND DELIGHT CLI APP"""
    pass


@main.command()
def add_recipe():
    """ ADD A RECIPE"""

    name = click.prompt("Enter the name of the recipe")
    description = click.prompt("Enter the description")
    cooking_time = click.prompt("Enter the cooking time")

    recipe = Recipe(name=name, description=description, cooking_time=cooking_time)
    session.add(recipe)
    session.commit()

    click.echo(f"Recipe '{recipe.name}' added successfully!!")

@main.command()

def add_ingredients():

    """ADD AN INGREDIENT"""

    name= click.prompt("Enter the name of the ingredient")
    quantity= click.prompt("Enter the quantity")
    units= click.prompt("Enter the units eg grams")

    # create the record

    ingredient= Ingredient(name=name, quantity=quantity, units=units)
    session.add(ingredient)
    session.commit()

# the name of the recipe to associate the ingredient with
    recipe_name = click.prompt("Enter the name of the recipe to associate this ingredient")

    # get the recipe name that has been entered
    recipe=session.query(Recipe).filter_by(name=recipe_name).first()

    if recipe:
        # If the recipe exists, create a new RecipeIngredient record 
        recipe_ingredient = RecipeIngredient(recipe_id=recipe.id, ingredient_id=ingredient.id, quantity=quantity, units=units)
        session.add(recipe_ingredient)
        session.commit()
        
        click.echo(f"Ingredient '{ingredient.name}' added to recipe '{recipe.name}' successfully!")
    else:
        click.echo(f"Recipe '{recipe_name}' not found. Please check the recipe name and try again.")

#  adding categories
@main.command()
def add_category():

    """ADD THE CATEGORY OF THE RECIPE"""
    name = click.prompt("Enter the category of the Recipe")
    category= Category(name=name)

    session.add(category)
    session.commit()


@main.command()

def list_categories():
    """SHOW THE LIST OF ALL CATEGORIES"""
    categories=session.query(Category).all()
    click.echo("The Recipe Categories are :")
    for category in categories :
        click.echo(f"-{category.name}")


@main.command()

def add_category_to_recipe():
    """ADD A CATEGORY TO A RECIPE"""

    recipe_name = click.prompt("Enter the name of the recipe")
    category_name = click.prompt("Enter the name of the category to add")
    
    recipe = session.query(Recipe).filter_by(name=recipe_name).first()
    category = session.query(Category).filter_by(name=category_name).first()
     

    if not recipe or not category:
        click.echo(" Please Enter the Right Category and Recipe")
    else:
        recipe.categories.append(category)
        session.commit()
        click.echo(f"Category '{category.name}' added to recipe '{recipe.name}'.")


        # displaying all the ingredients availabe

@main.command()
def list_recipes():
    """LIST ALL RECIPES AND THEIR DETAILS"""

    recipes=session.query(Recipe).all()


    if not recipes:
        click.echo("There are no recipes found!!")

    else:
        click.echo("All Recipes:")
        for recipe in recipes:
            click.echo(f"Name: {recipe.name}")
            click.echo(f"Description: {recipe.description}")
            click.echo(f"Cooking Time: {recipe.cooking_time} minutes")




# dipslaying ingredients for specific recipes
@main.command()

def display_ingredients():
    """DISPLAYING INGREDIENTS OF A SPECIFIC RECIPE"""

    recipe_name= click.echo("Enter  recipe name to find ingredients")

    recipe=session.query(Recipe).filter_by(name=recipe_name).first()

    if recipe:
        click.echo(f"Ingredients for '{recipe.name}' are : ")
        for ingredient in recipe.ingredients:
            click.echo(f"- {ingredient.name}: {ingredient.quantity} , {ingredient.units}")
    else:
        click.echo(f"Recipe '{recipe_name}' not found. Please check the recipe name and try again.")


@main.command()
def update_recipe():
    """Update an existing recipe."""
    recipe_name = click.prompt("Enter the name of the recipe to update")

    # Retrieve the recipe with the given name
    recipe = session.query(Recipe).filter_by(name=recipe_name).first()

    if recipe:
        new_name = click.prompt("Enter the new name of the recipe (leave empty to keep the same)")
        new_description = click.prompt("Enter the new description (leave empty to keep the same)")
        new_cooking_time = click.prompt("Enter the new cooking time (leave empty to keep the same)")

        if new_name:
            recipe.name = new_name
        if new_description:
            recipe.description = new_description
        if new_cooking_time:
            recipe.cooking_time = new_cooking_time

        session.commit()
        click.echo(f"Recipe '{recipe_name}' updated successfully!")
    else:
        click.echo(f"Recipe '{recipe_name}' not found. Please check the recipe name and try again.")

@main.command()
def delete_recipe():
    """DELETE A CERTAIN RECIPE."""
    recipe_name = click.prompt("Enter the name of the recipe to delete")

    # Retrieve the recipe with the given name
    recipe = session.query(Recipe).filter_by(name=recipe_name).first()

    if recipe:
        # Remove the recipe from associated categories
        for category in recipe.categories:
            category.recipes.remove(recipe)

        session.delete(recipe)
        session.commit()
        click.echo(f"Recipe '{recipe_name}' deleted successfully!")
    else:
        click.echo(f"Recipe '{recipe_name}' not found. Please check the recipe name and try again.")



if __name__=="__main__":
    main()