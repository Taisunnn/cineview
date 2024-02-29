from sqlalchemy import Column, Integer, String

from app.core.database import Base

class Login(Base):
    __tablename__ = "Login"
    login_id = Column(
        Integer(),
        primary_key=True,
        index=True
    )
    username = Column(String(), unique=True)
    hashed_password = Column(String())