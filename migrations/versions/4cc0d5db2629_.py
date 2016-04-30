"""empty message

Revision ID: 4cc0d5db2629
Revises: None
Create Date: 2016-04-26 23:42:24.470833

"""

# revision identifiers, used by Alembic.
revision = '4cc0d5db2629'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('location',
    sa.Column('provider_id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=100), nullable=True),
    sa.Column('street_address', sa.String(length=200), nullable=True),
    sa.Column('state', sa.String(length=2), nullable=True),
    sa.Column('zip_code', sa.Integer(), nullable=True),
    sa.Column('longitude', sa.Numeric(precision=12, scale=8), nullable=True),
    sa.Column('latitude', sa.Numeric(precision=12, scale=8), nullable=True),
    sa.PrimaryKeyConstraint('provider_id')
    )
    op.create_table('provider',
    sa.Column('provider_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('is_hospital', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('provider_id')
    )
    op.create_table('diagnosis',
    sa.Column('procedure', sa.String(length=200), nullable=False),
    sa.Column('provider_id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('avg_total_payments', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('avg_medicare_payments', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('avg_covered_charges', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('total_discharge', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['provider_id'], ['provider.provider_id'], ),
    sa.PrimaryKeyConstraint('procedure', 'provider_id', 'year')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('diagnosis')
    op.drop_table('provider')
    op.drop_table('location')
    ### end Alembic commands ###