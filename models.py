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
    N = "Not Completed"
    Y = "Completed"


class Task(BaseModel):
    id: UUID = uuid4()
    desc: str
    status: Status = Status.N


class NewTaskType(BaseModel):
    description: str
