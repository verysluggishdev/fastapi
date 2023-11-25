"""add content column to posts table 

Revision ID: b590be390a68
Revises: b3890ba57605
Create Date: 2023-11-25 16:18:03.666504

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b590be390a68'
down_revision: Union[str, None] = 'b3890ba57605'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
