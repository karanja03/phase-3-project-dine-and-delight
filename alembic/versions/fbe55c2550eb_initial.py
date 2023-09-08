"""initial

Revision ID: fbe55c2550eb
Revises: 
Create Date: 2023-09-08 09:08:04.974737

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fbe55c2550eb'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipe_step')
    op.drop_table('stepstofollow')
    op.add_column('ingredients', sa.Column('quantity', sa.String(), nullable=True))
    op.add_column('ingredients', sa.Column('units', sa.String(), nullable=True))
    op.alter_column('recipe_category', 'recipe_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('recipe_category', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('recipe_category', 'id')
    op.alter_column('recipe_ingredient', 'recipe_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('recipe_ingredient', 'ingredient_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('recipe_ingredient', 'id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe_ingredient', sa.Column('id', sa.INTEGER(), nullable=False))
    op.alter_column('recipe_ingredient', 'ingredient_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('recipe_ingredient', 'recipe_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.add_column('recipe_category', sa.Column('id', sa.INTEGER(), nullable=False))
    op.alter_column('recipe_category', 'category_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('recipe_category', 'recipe_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('ingredients', 'units')
    op.drop_column('ingredients', 'quantity')
    op.create_table('stepstofollow',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('description', sa.VARCHAR(), nullable=True),
    sa.Column('recipeId', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['recipeId'], ['recipes.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipe_step',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('recipe_id', sa.INTEGER(), nullable=True),
    sa.Column('step_id', sa.INTEGER(), nullable=True),
    sa.Column('step_order', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipes.id'], ),
    sa.ForeignKeyConstraint(['step_id'], ['stepstofollow.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
