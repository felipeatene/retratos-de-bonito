"""add users and roles tables

Revision ID: a3f5c8d9e1b2
Revises: 81d2543caf84
Create Date: 2025-12-26 10:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3f5c8d9e1b2'
down_revision: Union[str, None] = '81d2543caf84'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Criar tabela de papéis
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=50), nullable=False),
        sa.Column('description', sa.String(length=255), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    
    # Criar tabela de usuários
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('email', sa.String(length=255), nullable=False),
        sa.Column('password_hash', sa.String(length=255), nullable=False),
        sa.Column('role_id', sa.Integer(), nullable=True),
        sa.Column('is_active', sa.Boolean(), nullable=False, default=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    
    # Adicionar coluna contributor_id na tabela photos usando batch mode (SQLite)
    with op.batch_alter_table('photos') as batch_op:
        batch_op.add_column(
            sa.Column('contributor_id', sa.Integer(), nullable=True)
        )
        batch_op.create_foreign_key(
            'fk_photos_contributor_id',
            'users',
            ['contributor_id'], ['id']
        )
    
    # Inserir papéis padrão
    op.execute(
        "INSERT INTO roles (name, description) VALUES "
        "('user', 'Contribuidor - pode enviar fotos e acompanhar contribuições'), "
        "('curator', 'Curador - pode fazer curadoria, validar fotos e gerenciar histórias'), "
        "('admin', 'Administrador - acesso total ao sistema')"
    )


def downgrade() -> None:
    # Remover foreign key e coluna contributor_id usando batch mode
    with op.batch_alter_table('photos') as batch_op:
        batch_op.drop_constraint('fk_photos_contributor_id', type_='foreignkey')
        batch_op.drop_column('contributor_id')
    
    # Remover tabelas
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('roles')
