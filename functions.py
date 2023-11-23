import classes
from datetime import date
import db


def add(user_id:int='user_id', category:str='category', description:str='description', date:date=date):
    task = classes.Task(user_id=user_id, category=category, description=description, date=date)
    db.save_add(task)

def sign_up(username:str='username', password:int='password'):
    new_user = classes.User(username=username, password=password)
    users_list = db.users_list()
    users_list.append(new_user)
    db.save_user(users_list)

def delete(user_id:int='user_id', category:str='category', description:str='description', date:date=date):
    task = classes.Task(user_id=user_id, category=category, description=description, date=date)
    db.save_delete(task)

def to_update(user_id:int='user_id', category:str='category', description:str='description', date:date=date):
    task = classes.Task(user_id=user_id, category=category, description=description, date=date)
    db.get_task_id(user_id=user_id, category=category, description=description, date=date)

def update(user_id:int='user_id', category:str='category', description:str='description', date:date=date):
    task = classes.Task(user_id=user_id, category=category, description=description, date=date)
    db.save_new_update(task)
   
def search(user_id:int='user_id', query:str='query'):
    tasks = db.get_dicts(user_id)
    results = []
    for task in tasks:
        if query in task["user_id"] or query in task["category"] or query in task["description"] or query in task["date"]:            results.append(task)
    return results


    