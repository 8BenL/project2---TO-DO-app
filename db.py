import sqlite3
from datetime import date
from classes import Task


def setup(filename="tasks.sqlite"):
    with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tasks(category TEXT, description TEXT, date DATE)")
        conn.commit()


def query_db(sql, filename="tasks.sqlite"):
     with sqlite3.connect(filename) as conn:
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return cur.fetchall()
     
def get_dicts():
    tasks = query_db("SELECT * FROM tasks")
    keys = ["category", "description", "date"]
    tasks_list = []
    for task in tasks:
        values = list(task)
        dict_row = dict(zip(keys, values))
        tasks_list.append(dict_row)
    return tasks_list


def get_objects():
        tasks = query_db("SELECT * FROM tasks")
        objects_list = []
        for task in tasks:
             task = Task(task[0], task[1], task[2])                                  
             objects_list.append(task)
        return objects_list
             

def load():
    tasks = get_dicts()
    today_tasks = []
    for task in tasks:
        if task['date'] == str(date.today()):
            today_tasks.append(task)
    return today_tasks


def save(tasks_list:list):
    query_db(f"DELETE FROM tasks")
    for task in tasks_list:
        query_db(f"INSERT INTO tasks VALUES ('{task.category}','{task.description}','{task.date}')")
        
        
    '''tasks = get_objects()
        task = Task(category="category", description="description", date=date)
        dates = []
        for task in tasks:
            dates.append(task.date)
        dates.sort'''
    

'''def tasks_list():
    dicts_list = get_dicts()
    tasks = []
    for task in tasks:
        if task['date'] < str(date.today()):
            tasks.append(task)
    return tasks'''

    



