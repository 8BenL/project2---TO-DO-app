import classes
from datetime import date
import db


def add(user_id:int='user_id', category:str='category', description:str='description', date:date=date):
    tasks_list = db.get_objects(user_id)
    task = classes.Task(user_id=user_id, category=category, description=description, date=date)
    new_tasks_list = tasks_list.append(task)
    db.save(new_tasks_list)

def sign_up(username:str='username', password:int='password'):
    new_user = classes.User(username=username, password=password)
    users_list = db.users_list()
    users_list.append(new_user)
    db.save_user(users_list)


def delete(user_id:int='user_id', category:str='category', description:str='description', date:date=date):
    tasks_list = db.get_objects(user_id)
    task = classes.Task(user_id=user_id, category=category, description=description, date=date)
    for task in tasks_list:
        if task.category == category and task.description == description and task.date == date:
            tasks_list.remove(task)
    db.save(tasks_list)
    return tasks_list


def to_update(user_id:int='user_id', category:str='category', description:str='description', date:date=date):
    tasks_list = db.get_objects(user_id)
    task = classes.Task(user_id=user_id, category=category, description=description, date=date)
    for task in tasks_list:
        if task.category == category and task.description == description and task.date == date:
            tasks_list.remove(task)
    db.save(tasks_list)
    return tasks_list


def update(user_id:int='user_id', category:str='category', description:str='description', date:date=date):
    tasks_list = db.get_objects(user_id)
    task = classes.Task(user_id=user_id, category=category, description=description, date=date)
    tasks_list.append(task)
    db.save(tasks_list)
    return tasks_list


def search(user_id:int='user_id', query:str='query'):
    tasks = db.get_objects(user_id)
    results = []
    for task in tasks:
        if query in task.category or query in task.description or query in task.date:
            results.append(task)
    return results


    