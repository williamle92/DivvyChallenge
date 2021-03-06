"""empty message

Revision ID: b80821e6bdb4
Revises: 
Create Date: 2021-06-16 20:29:08.531109

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b80821e6bdb4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('divvy',
    sa.Column('trip_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('stop_time', sa.DateTime(), nullable=False),
    sa.Column('bike_id', sa.Integer(), nullable=False),
    sa.Column('from_station_id', sa.Integer(), nullable=False),
    sa.Column('from_station_name', sa.String(length=100), nullable=False),
    sa.Column('to_station_id', sa.Integer(), nullable=False),
    sa.Column('to_station_name', sa.String(length=100), nullable=False),
    sa.Column('user_type', sa.String(length=40), nullable=False),
    sa.Column('gender', sa.String(length=30), nullable=True),
    sa.Column('birthday', sa.String(length=50), nullable=True),
    sa.Column('trip_duration', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('trip_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('divvy')
    # ### end Alembic commands ###
