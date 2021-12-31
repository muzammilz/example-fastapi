"""add foreign key to posts table

Revision ID: 508ca4650bfb
Revises: 128470527f68
Create Date: 2021-12-28 16:34:03.109663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '508ca4650bfb'
down_revision = '128470527f68'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('posts_users_fk', source_table ="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="Cascade")
    pass


def downgrade():
    op.drop_constraint('posts_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
