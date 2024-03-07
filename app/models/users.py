from sqlalchemy import Column, Integer, String

from app.core.database import Base

class Users(Base):

    __tablename__ = "Users"

    user_id = Column(
        "user_id",
        Integer(),
        nullable=False,
        primary_key=True
    )
    first_name = Column("first_name", String(), nullable=False)
    last_name = Column("last_name", String(), nullable=False)
    age = Column("age", Integer(), nullable=False)
    gender = Column("gender", String(), nullable=False)