from enum import Enum
from tkinter import N
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel


class User(BaseModel):
    name:str
    email:str
    password:str
    age:int
    id: UUID = uuid4()

class Status(str, Enum):
    N = "Not Completed"
    Y = "Completed"

class Task(BaseModel):
    id:UUID = uuid4()
    desc:str  
    status:Status = Status.N
    #Having issues getting the addition of tasks using description only, also the enum wahala

class NewTaskType(BaseModel):
    description: str 