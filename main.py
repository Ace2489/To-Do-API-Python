from hashlib import new
from tkinter import N
from fastapi import FastAPI
from models import User, Task, NewTaskType, Status

app = FastAPI()

Users:list[User] = [User(name = "John Paul", email = "mahio4u@yahoo.com", password = 1234, age = 23)]
Tasks:list[Task] = [Task(id = "56bc791c-11ea-4a18-9769-374d675f1270",
    desc = "reading book",
    status = Status.N)]

@app.get("/users")
def get_users():
    return Users

@app.post("/user/register")
def register_user(user:User):
    Users.append(user)

@app.delete("/user/moi")
def delete_user(user:User):
    Users.remove(user)  

@app.post("/task")
def new_task(task:NewTaskType):
    new_task = Task(desc = task.description)
    Tasks.append(new_task)

@app.get("/task")
def get_tasks():
    return Tasks

