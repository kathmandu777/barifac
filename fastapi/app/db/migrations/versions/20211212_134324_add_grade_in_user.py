"""add_grade_in_user

Revision ID: 1595a2312b55
Revises: 439129fe7774
Create Date: 2021-12-12 13:43:24.763054+09:00

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "1595a2312b55"
down_revision = "439129fe7774"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("grade", sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "grade")
    # ### end Alembic commands ###
