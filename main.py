from uuid import UUID
from fastapi import FastAPI
from models import User, Task, NewTaskType, Status, TaskUpdate

app = FastAPI()

Users: list[User] = [User(name="John Paul", email="mahio4u@yahoo.com", password=1234, age=23)]
Tasks: list[Task] = [Task(id="56bc791c-11ea-4a18-9769-374d675f1270",
                          desc="reading book",
                          status=Status.false)]


@app.get("/users")
def get_users():
    return Users


@app.post("/user/register")
def register_user(user: User):
    Users.append(user)

@app.get("/task/")
def get_tasks():
    return Tasks


@app.delete("/user/moi")
def delete_user(user: User):
    Users.remove(user)


@app.post("/task")
def task_creator(task: NewTaskType):
    new_task = Task(desc=task.description)
    Tasks.append(new_task)




@app.get("/task/{task_id}")
def get_task_by_id(task_id: UUID):
    for task in Tasks:
        if task.id == task_id:
            return task


@app.get("/task")
def get_task_by_status(completed: Status):
    for task in Tasks:
        if task.completed == completed:
            return task

@app.put("/task/{task_id}")
def update_task_by_id(task_id:UUID, status:TaskUpdate):
    for task in Tasks:
        if task_id == task.id:
            task.completed = status.completed

@app.delete("/task/{task_id}")
def delete_task_by_id(task_id:UUID):
    for task in Tasks:
        if task_id == task.id:
            Tasks.remove(task)