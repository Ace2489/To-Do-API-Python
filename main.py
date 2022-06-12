from hashlib import new
from fastapi import FastAPI
from models import User, Task, NewTaskType

app = FastAPI()

Users:list[User] = [User(name = "John Paul", email = "mahio4u@yahoo.com", password = 1234, age = 23)]
Tasks:list[Task] = []

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

