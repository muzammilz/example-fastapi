"""add user table

Revision ID: 128470527f68
Revises: a71eb853e774
Create Date: 2021-12-28 16:23:32.548161

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '128470527f68'
down_revision = 'a71eb853e774'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
