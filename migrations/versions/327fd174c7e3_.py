"""empty message

Revision ID: 327fd174c7e3
Revises: 3bc5447170ff
Create Date: 2022-05-20 20:24:39.324136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '327fd174c7e3'
down_revision = '3bc5447170ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
