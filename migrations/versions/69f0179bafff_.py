"""empty message

Revision ID: 69f0179bafff
Revises: 74cd055978ab
Create Date: 2020-07-04 11:27:08.957428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69f0179bafff'
down_revision = '74cd055978ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('website', sa.String(length=500), nullable=True))
    op.drop_column('Venue', 'seeking_artist')
    op.drop_column('Venue', 'seeking_artist_request')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('seeking_artist_request', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    op.add_column('Venue', sa.Column('seeking_artist', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('Venue', 'website')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'seeking_description')
    # ### end Alembic commands ###
