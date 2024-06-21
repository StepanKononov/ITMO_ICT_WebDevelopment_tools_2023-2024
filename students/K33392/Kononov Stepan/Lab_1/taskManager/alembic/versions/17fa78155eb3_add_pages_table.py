"""Add pages table

Revision ID: 17fa78155eb3
Revises: e5d4f41a1cfd
Create Date: 2024-06-19 00:07:29.107397

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17fa78155eb3'
down_revision: Union[str, None] = 'e5d4f41a1cfd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_pages_url', table_name='pages')
    op.create_index(op.f('ix_pages_url'), 'pages', ['url'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_pages_url'), table_name='pages')
    op.create_index('ix_pages_url', 'pages', ['url'], unique=True)
    # ### end Alembic commands ###