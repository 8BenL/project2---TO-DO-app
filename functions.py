from classes import Task
from datetime import date
import db


def add(category:str='category', description:str='description', date:date=date):
    tasks_list = db.get_objects()
    task = Task(category=category, description=description, date=date)
    tasks_list.append(task)
    db.save(tasks_list)


def delete(category:str='category', description:str='description', date:date=date):
    tasks_list = db.get_objects()
    task = Task(category=category, description=description, date=date)
    for task in tasks_list:
        if task.category == category and task.description == description and task.date == date:
            tasks_list.remove(task)
    db.save(tasks_list)
    return tasks_list


def to_update(category:str='category', description:str='description', date:date=date):
    tasks_list = db.get_objects()
    task = Task(category=category, description=description, date=date)
    for task in tasks_list:
        if task.category == category and task.description == description and task.date == date:
            tasks_list.remove(task)
    db.save(tasks_list)
    return tasks_list


def update(category:str='category', description:str='description', date:date=date):
    tasks_list = db.get_objects()
    task = Task(category=category, description=description, date=date)
    tasks_list.append(task)
    db.save(tasks_list)
    return tasks_list


def search(query:str='query'):
    tasks = db.get_objects()
    results = []
    for task in tasks:
        if query in task.category or query in task.description or query in task.date:
            results.append(task)
    return results


    