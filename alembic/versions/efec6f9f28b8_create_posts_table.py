"""create posts table

Revision ID: efec6f9f28b8
Revises: 
Create Date: 2021-12-24 17:27:13.082913

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efec6f9f28b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer, nullable = False, primary_key=True)
                    , sa.Column('title', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
