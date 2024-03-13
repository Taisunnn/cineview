from pydantic import BaseModel


class Titles(BaseModel):
    title_id: int
    title_name: str
    score: float
    synopsis: str
    episodes: int
