"""对所有外键设置了级联删除

Revision ID: 1b3cb02d23e2
Revises: d0530f9b2fc5
Create Date: 2024-06-12 19:47:10.620486

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b3cb02d23e2'
down_revision: Union[str, None] = 'd0530f9b2fc5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
