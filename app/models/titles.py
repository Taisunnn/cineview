from sqlalchemy import Column, Integer, String, Float

from app.core.database import Base


class Titles(Base):

    __tablename__ = "titles"

    title_id = Column("title_id", Integer(), primary_key=True)
    title_name = Column("title_name", String())
    score = Column("score", Float())
    synopsis = Column("synopsis", String())
    episodes = Column("episodes", Integer())
