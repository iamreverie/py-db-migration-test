"""create logs table

Revision ID: bee0f0fe6ad9
Revises: 
Create Date: 2025-09-24 21:07:27.129609

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import datetime


# revision identifiers, used by Alembic.
revision: str = 'bee0f0fe6ad9'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'logs',
        sa.Column('id', sa.BigInteger(), autoincrement=True, primary_key=True),
        sa.Column('action', sa.String(50), nullable=False),
        sa.Column('context', sa.Text()),
        sa.Column('path', sa.String(260), nullable=True),
        sa.Column('row_number', sa.Integer, nullable=True),
        sa.Column('created', sa.DateTime, default=datetime.datetime.utcnow, nullable=False),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('logs')
