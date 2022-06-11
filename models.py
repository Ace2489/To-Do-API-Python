from uuid import UUID, uuid4
from pydantic import BaseModel


class User(BaseModel):
    name:str
    email:str
    password:str
    age:int
    id: UUID = uuid4()

class Task(BaseModel):
    #id, Completed_stats
    id:UUID = uuid4()


