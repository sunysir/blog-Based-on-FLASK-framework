"""empty message

Revision ID: 8019de1f599c
Revises: 9f497da5c619
Create Date: 2018-05-21 19:13:20.215187

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8019de1f599c'
down_revision = '9f497da5c619'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.Column('passwd_hash', sa.String(length=128), nullable=True),
    sa.Column('birthday', sa.DATE(), nullable=True),
    sa.Column('email', sa.String(length=32), nullable=True),
    sa.Column('head_picture', sa.String(length=128), nullable=True),
    sa.Column('confirmed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('birthday'),
    sa.UniqueConstraint('passwd_hash'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
