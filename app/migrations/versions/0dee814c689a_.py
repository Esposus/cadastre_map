"""empty message

Revision ID: 0dee814c689a
Revises: 
Create Date: 2023-10-22 14:26:15.074062

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0dee814c689a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cadastre_queries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cadastre_number', sa.Integer(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('result', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_cadastre_queries_cadastre_number'), 'cadastre_queries', ['cadastre_number'], unique=False)
    op.create_index(op.f('ix_cadastre_queries_id'), 'cadastre_queries', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cadastre_queries_id'), table_name='cadastre_queries')
    op.drop_index(op.f('ix_cadastre_queries_cadastre_number'), table_name='cadastre_queries')
    op.drop_table('cadastre_queries')
    # ### end Alembic commands ###
