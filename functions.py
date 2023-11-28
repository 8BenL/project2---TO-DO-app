import classes
from datetime import date
import db


def add(user_id:int='user_id', category:str='category', description:str='description', date:date=date):
    task = classes.Task(user_id=user_id, category=category, description=description, date=date)
    db.save_add(task)            

def delete(user_id:int='user_id', category:str='category', description:str='description', date:date=date):
    task = classes.Task(user_id=user_id, category=category, description=description, date=date)
    db.save_delete(task)

def update(task_id:int, user_id:int='user_id', category:str='category', description:str='description', date:date=date):
    task = classes.Task(id=task_id, user_id=user_id, category=category, description=description, date=date)
    db.save_new_update(task)
    return task

def toggle_task(task_id:int,completed:int):
    db.toggle_task(task_id=task_id, completed=completed)
   
def search(user_id, query):
    tasks = db.get_objects(user_id)
    results = []
    for task in tasks:
        if query in task.category or query in task.description or query in task.date:
            results.append(task)
    return results


    