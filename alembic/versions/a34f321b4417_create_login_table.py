"""create login table

Revision ID: a34f321b4417
Revises: 
Create Date: 2024-03-12 22:20:31.930527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "a34f321b4417"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "Login",
        sa.Column(
            "login_id", sa.Integer(), primary_key=True, index=True, autoincrement=True
        ),
        sa.Column("username", sa.String(15), unique=True),
        sa.Column("hashed_password", sa.String(255)),
    )


def downgrade() -> None:
    op.drop_table("Login")
