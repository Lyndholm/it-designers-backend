"""remove additional_name column

Revision ID: 5f2d8fcb98fa
Revises: 64a78d63529c
Create Date: 2022-05-18 15:54:56.768566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5f2d8fcb98fa'
down_revision = '64a78d63529c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'additional_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('additional_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###