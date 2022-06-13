from enum import Enum
from uuid import UUID, uuid4

from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str
    age: int
    id: UUID = uuid4()


class Status(str, Enum):
    true = "True"
    false = "False"


class Task(BaseModel):
    id: UUID = uuid4()
    desc: str
    completed: Status = Status.false


class NewTaskType(BaseModel):
    description: str

class TaskUpdate(BaseModel):
    completed:Status