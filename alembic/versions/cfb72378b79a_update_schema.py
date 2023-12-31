"""Update schema

Revision ID: cfb72378b79a
Revises: ebd2a0bd521b
Create Date: 2023-09-08 09:53:08.536571

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cfb72378b79a'
down_revision: Union[str, None] = 'ebd2a0bd521b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
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
    # ### end Alembic commands ###
