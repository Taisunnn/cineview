from pydantic import BaseModel

class Users(BaseModel):
    first_name: str
    last_name: str
    age: int
    gender: str