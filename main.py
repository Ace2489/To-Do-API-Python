from fastapi import FastAPI
from models import User

app = FastAPI()

Users:list[User] = [User(name = "John Paul", email = "mahio4u@yahoo.com", password = 1234, age = 23)]


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
def new_task():
    pass