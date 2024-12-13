"""Add alpn and other networks to InboundConfig

Revision ID: a00786a4da47
Revises: c78517599f01
Create Date: 2024-11-27 20:50:20.606559

"""

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "a00786a4da47"
down_revision = "c78517599f01"
branch_labels = None
depends_on = None

# Describing of enum
enum_name = "inboundnetwork"
temp_enum_name = f"temp_{enum_name}"
old_values = ("tcp", "ws", "grpc")
new_values = ("kcp", "http", "httpupgrade", "splithttp", *old_values)

old_type = sa.Enum(*old_values, name=enum_name)
new_type = sa.Enum(*new_values, name=enum_name)
temp_type = sa.Enum(*new_values, name=temp_enum_name)

# Describing of table
table_name = "inbound_config"
column_name = "network"


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "inbound_config", sa.Column("alpn", sa.String(length=400), nullable=True)
    )

    # temp type to use instead of old one
    temp_type.create(op.get_bind(), checkfirst=False)
    op.execute("ALTER TABLE inbound_config ALTER COLUMN network DROP DEFAULT")

    # changing of column type from old enum to new one.
    # SQLite will create temp table for this
    with op.batch_alter_table(table_name) as batch_op:
        batch_op.alter_column(
            column_name,
            existing_type=old_type,
            type_=temp_type,
            existing_nullable=False,
            postgresql_using=f"{column_name}::text::{temp_enum_name}",
        )

    # remove old enum, create new enum
    old_type.drop(op.get_bind(), checkfirst=False)
    new_type.create(op.get_bind(), checkfirst=False)

    # changing of column type from temp enum to new one.
    # SQLite will create temp table for this
    with op.batch_alter_table(table_name) as batch_op:
        batch_op.alter_column(
            column_name,
            existing_type=temp_type,
            type_=new_type,
            existing_nullable=False,
            postgresql_using=f"{column_name}::text::{enum_name}",
        )

    # remove temp enum
    temp_type.drop(op.get_bind(), checkfirst=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("inbound_config", "alpn")
    # ### end Alembic commands ###