"""empty message

Revision ID: e0601401bcb4
Revises: 3b02be6e2287
Create Date: 2020-03-15 13:39:52.605227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0601401bcb4'
down_revision = '3b02be6e2287'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('revoked_access_tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jti', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('revoked_access_tokens')
    # ### end Alembic commands ###
