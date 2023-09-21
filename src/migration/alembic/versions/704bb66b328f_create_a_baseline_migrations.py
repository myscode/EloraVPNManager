"""Create a baseline migrations

Revision ID: 704bb66b328f
Revises: 
Create Date: 2023-08-14 13:21:15.265449

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '704bb66b328f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('host',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=128), nullable=True),
                    sa.Column('domain', sa.String(length=128), nullable=True),
                    sa.Column('username', sa.String(length=34), nullable=True),
                    sa.Column('password', sa.String(length=128), nullable=True),
                    sa.Column('ip', sa.String(length=128), nullable=True),
                    sa.Column('port', sa.Integer(), nullable=True),
                    sa.Column('api_path', sa.String(length=400), nullable=True),
                    sa.Column('enable', sa.Boolean(), nullable=True),
                    sa.Column('master', sa.Boolean(), nullable=True),
                    sa.Column('type', sa.Enum('x_ui_sanaei', 'x_ui_kafka', name='hosttype'), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('modified_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_host_domain'), 'host', ['domain'], unique=True)
    op.create_index(op.f('ix_host_id'), 'host', ['id'], unique=False)
    op.create_index(op.f('ix_host_ip'), 'host', ['ip'], unique=True)
    op.create_index(op.f('ix_host_name'), 'host', ['name'], unique=False)
    op.create_index(op.f('ix_host_port'), 'host', ['port'], unique=False)
    op.create_table('user',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(length=128), nullable=False),
                    sa.Column('hashed_password', sa.String(length=128), nullable=True),
                    sa.Column('first_name', sa.String(length=128), nullable=True),
                    sa.Column('last_name', sa.String(length=128), nullable=True),
                    sa.Column('description', sa.String(length=4000), nullable=True),
                    sa.Column('telegram_chat_id', sa.BigInteger(), nullable=True),
                    sa.Column('telegram_username', sa.String(length=128), nullable=True),
                    sa.Column('phone_number', sa.String(length=128), nullable=True),
                    sa.Column('email_address', sa.String(length=128), nullable=True),
                    sa.Column('enable', sa.Boolean(), nullable=True),
                    sa.Column('banned', sa.Boolean(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('modified_at', sa.DateTime(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('telegram_chat_id')
                    )
    op.create_index(op.f('ix_user_email_address'), 'user', ['email_address'], unique=True)
    op.create_index(op.f('ix_user_first_name'), 'user', ['first_name'], unique=False)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_index(op.f('ix_user_last_name'), 'user', ['last_name'], unique=False)
    op.create_index(op.f('ix_user_phone_number'), 'user', ['phone_number'], unique=True)
    op.create_index(op.f('ix_user_telegram_username'), 'user', ['telegram_username'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('account',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=True),
                    sa.Column('uuid', sa.String(length=128), nullable=False),
                    sa.Column('email', sa.String(length=128), nullable=False),
                    sa.Column('enable', sa.Boolean(), nullable=True),
                    sa.Column('used_traffic', sa.BigInteger(), nullable=True),
                    sa.Column('data_limit', sa.BigInteger(), nullable=True),
                    sa.Column('expired_at', sa.DateTime(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('modified_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_account_email'), 'account', ['email'], unique=True)
    op.create_index(op.f('ix_account_id'), 'account', ['id'], unique=False)
    op.create_index(op.f('ix_account_uuid'), 'account', ['uuid'], unique=True)
    op.create_table('inbound',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('host_id', sa.Integer(), nullable=True),
                    sa.Column('key', sa.Integer(), nullable=False),
                    sa.Column('remark', sa.String(length=128), nullable=True),
                    sa.Column('port', sa.Integer(), nullable=True),
                    sa.Column('domain', sa.String(length=128), nullable=True),
                    sa.Column('request_host', sa.String(length=128), nullable=True),
                    sa.Column('sni', sa.String(length=128), nullable=True),
                    sa.Column('address', sa.String(length=128), nullable=True),
                    sa.Column('path', sa.String(length=400), nullable=True),
                    sa.Column('enable', sa.Boolean(), nullable=True),
                    sa.Column('develop', sa.Boolean(), nullable=True),
                    sa.Column('security', sa.Enum('default', 'none', name='inboundsecurity'), nullable=False),
                    sa.Column('type', sa.Enum('default', 'VMess', 'Trojan', 'Shadowsocks', name='inboundtype'),
                              nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('modified_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['host_id'], ['host.id'], ),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('host_id', 'key')
                    )
    op.create_index(op.f('ix_inbound_address'), 'inbound', ['address'], unique=False)
    op.create_index(op.f('ix_inbound_domain'), 'inbound', ['domain'], unique=False)
    op.create_index(op.f('ix_inbound_id'), 'inbound', ['id'], unique=False)
    op.create_index(op.f('ix_inbound_key'), 'inbound', ['key'], unique=False)
    op.create_index(op.f('ix_inbound_port'), 'inbound', ['port'], unique=False)
    op.create_index(op.f('ix_inbound_remark'), 'inbound', ['remark'], unique=False)
    op.create_index(op.f('ix_inbound_request_host'), 'inbound', ['request_host'], unique=False)
    op.create_index(op.f('ix_inbound_sni'), 'inbound', ['sni'], unique=False)
    op.create_table('account_used_traffic',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('account_id', sa.Integer(), nullable=True),
                    sa.Column('download', sa.BigInteger(), nullable=True),
                    sa.Column('upload', sa.BigInteger(), nullable=True),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['account_id'], ['account.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_account_used_traffic_id'), 'account_used_traffic', ['id'], unique=False)
    op.create_table('inbound_config',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('inbound_id', sa.Integer(), nullable=True),
                    sa.Column('remark', sa.String(length=128), nullable=True),
                    sa.Column('port', sa.Integer(), nullable=True),
                    sa.Column('domain', sa.String(length=128), nullable=True),
                    sa.Column('host', sa.String(length=128), nullable=True),
                    sa.Column('sni', sa.String(length=128), nullable=True),
                    sa.Column('address', sa.String(length=128), nullable=True),
                    sa.Column('path', sa.String(length=400), nullable=True),
                    sa.Column('enable', sa.Boolean(), nullable=True),
                    sa.Column('develop', sa.Boolean(), nullable=True),
                    sa.Column('finger_print', sa.Enum('default', 'chrome', 'firefox', name='inboundfingerprint'),
                              nullable=False),
                    sa.Column('security', sa.Enum('default', 'none', name='inboundsecurity'), nullable=False),
                    sa.Column('type', sa.Enum('default', 'VMess', 'Trojan', 'Shadowsocks', name='inboundtype'),
                              nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('modified_at', sa.DateTime(), nullable=True),
                    sa.ForeignKeyConstraint(['inbound_id'], ['inbound.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_index(op.f('ix_inbound_config_address'), 'inbound_config', ['address'], unique=False)
    op.create_index(op.f('ix_inbound_config_domain'), 'inbound_config', ['domain'], unique=False)
    op.create_index(op.f('ix_inbound_config_host'), 'inbound_config', ['host'], unique=False)
    op.create_index(op.f('ix_inbound_config_id'), 'inbound_config', ['id'], unique=False)
    op.create_index(op.f('ix_inbound_config_port'), 'inbound_config', ['port'], unique=False)
    op.create_index(op.f('ix_inbound_config_remark'), 'inbound_config', ['remark'], unique=False)
    op.create_index(op.f('ix_inbound_config_sni'), 'inbound_config', ['sni'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_inbound_config_sni'), table_name='inbound_config')
    op.drop_index(op.f('ix_inbound_config_remark'), table_name='inbound_config')
    op.drop_index(op.f('ix_inbound_config_port'), table_name='inbound_config')
    op.drop_index(op.f('ix_inbound_config_id'), table_name='inbound_config')
    op.drop_index(op.f('ix_inbound_config_host'), table_name='inbound_config')
    op.drop_index(op.f('ix_inbound_config_domain'), table_name='inbound_config')
    op.drop_index(op.f('ix_inbound_config_address'), table_name='inbound_config')
    op.drop_table('inbound_config')
    op.drop_index(op.f('ix_account_used_traffic_id'), table_name='account_used_traffic')
    op.drop_table('account_used_traffic')
    op.drop_index(op.f('ix_inbound_sni'), table_name='inbound')
    op.drop_index(op.f('ix_inbound_request_host'), table_name='inbound')
    op.drop_index(op.f('ix_inbound_remark'), table_name='inbound')
    op.drop_index(op.f('ix_inbound_port'), table_name='inbound')
    op.drop_index(op.f('ix_inbound_key'), table_name='inbound')
    op.drop_index(op.f('ix_inbound_id'), table_name='inbound')
    op.drop_index(op.f('ix_inbound_domain'), table_name='inbound')
    op.drop_index(op.f('ix_inbound_address'), table_name='inbound')
    op.drop_table('inbound')
    op.drop_index(op.f('ix_account_uuid'), table_name='account')
    op.drop_index(op.f('ix_account_id'), table_name='account')
    op.drop_index(op.f('ix_account_email'), table_name='account')
    op.drop_table('account')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_telegram_username'), table_name='user')
    op.drop_index(op.f('ix_user_phone_number'), table_name='user')
    op.drop_index(op.f('ix_user_last_name'), table_name='user')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_first_name'), table_name='user')
    op.drop_index(op.f('ix_user_email_address'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_host_port'), table_name='host')
    op.drop_index(op.f('ix_host_name'), table_name='host')
    op.drop_index(op.f('ix_host_ip'), table_name='host')
    op.drop_index(op.f('ix_host_id'), table_name='host')
    op.drop_index(op.f('ix_host_domain'), table_name='host')
    op.drop_table('host')
    # ### end Alembic commands ###
