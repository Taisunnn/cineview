"""create titles table

Revision ID: 52259c20bfda
Revises: a34f321b4417
Create Date: 2024-03-12 23:08:16.899146

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "52259c20bfda"
down_revision = "a34f321b4417"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "titles",
        sa.Column("title_id", sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column("title_name", sa.String(255)),
        sa.Column("score", sa.Float()),
        sa.Column("synopsis", sa.String(1500)),
        sa.Column("episodes", sa.Integer()),
    )


def downgrade() -> None:
    op.drop_table("titles")
