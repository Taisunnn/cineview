from pydantic import BaseModel

class Movies(BaseModel):
    anime_id: int
    title: str
    score: float
    synopsis: str
    episodes: int