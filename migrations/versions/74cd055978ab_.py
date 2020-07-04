"""empty message

Revision ID: 74cd055978ab
Revises: 77ba6ab1fcc8
Create Date: 2020-07-04 11:02:27.255345

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74cd055978ab'
down_revision = '77ba6ab1fcc8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artist_to_genre_assocations',
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['Genre.id'], ),
    sa.PrimaryKeyConstraint('artist_id', 'genre_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('artist_to_genre_assocations')
    # ### end Alembic commands ###
