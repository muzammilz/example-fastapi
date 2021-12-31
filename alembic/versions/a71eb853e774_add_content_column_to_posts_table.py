"""add content column to posts table

Revision ID: a71eb853e774
Revises: efec6f9f28b8
Create Date: 2021-12-28 16:12:33.387305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a71eb853e774'
down_revision = 'efec6f9f28b8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
