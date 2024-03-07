from sqlalchemy import Column, Integer, String, Float

from app.core.database import Base

class Movies(Base):
    
    __tablename__ = 'movies'

    anime_id = Column(Integer(), primary_key = True)
    title = Column(String())
    score = Column(Float())
    synopsis = Column(String())
    episodes = Column(Integer())