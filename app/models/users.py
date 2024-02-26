import sqlalchemy as sa
from sqlalchemy.dialects import mysql

from app.core.database import Base

class Users(Base):
    __tablename__ = "Users"
    user_id = sa.Column(
        "user_id",
        sa.Integer(),
        nullable=False,
        primary_key=True
    )
    first_name = sa.Column("first_name", sa.String(), nullable=False)
    last_name = sa.Column("last_name", sa.String(), nullable=False)
    age = sa.Column("age", sa.Integer(), nullable=False)
    gender = sa.Column("gender", sa.String(), nullable=False)