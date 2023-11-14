"""rename department

Revision ID: 11968d06b3fb
Revises: 39a957610445
Create Date: 2023-11-14 13:16:01.555690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11968d06b3fb'
down_revision = '39a957610445'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###