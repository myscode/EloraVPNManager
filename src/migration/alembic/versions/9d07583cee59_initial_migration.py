"""Initial migration.

Revision ID: 9d07583cee59
Revises: 
Create Date: 2023-07-15 21:34:21.117606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d07583cee59'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account_used_traffic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('account_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_account_used_traffic_id'), 'account_used_traffic', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_account_used_traffic_id'), table_name='account_used_traffic')
    op.drop_table('account_used_traffic')
    # ### end Alembic commands ###
