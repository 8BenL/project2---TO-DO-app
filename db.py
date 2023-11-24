import sqlite3
from datetime import date
import classes


def query_db(sql):
     with sqlite3.connect('tasks.db') as conn:
        cur = conn.cursor()
        rows = cur.execute(sql).fetchall()
        return rows
       
def get_user_id(username="", password=""):
    return query_db(f"SELECT user_id FROM users WHERE username='{username}' AND password='{password}'")[0][0]

def get_username(user_id=""):
    return query_db(f"SELECT username FROM users WHERE user_id='{user_id}'")[0][0]

def login(username="", password=""):
    sql=f"SELECT user_id FROM users WHERE username='{username}' AND password='{password}'"
    if query_db(sql)==0:
        return False
    return True

def users_list():
    users = query_db(f"SELECT * FROM users")
    objects_list = []
    for user in users:
        user = classes.User(user[1], user[2])
        objects_list.append(user)
    return objects_list

def get_dicts(user_id):
    tasks = query_db(f"SELECT * FROM tasks WHERE user_id='{user_id}'")
    keys = ["id", "user_id", "category", "description", "date"]
    tasks_list = []
    for task in tasks:
        values = list(task)
        dict_row = dict(zip(keys, values))
        tasks_list.append(dict_row)
    return tasks_list

def get_objects(user_id):
    tasks = query_db(f"SELECT * FROM tasks WHERE user_id='{user_id}'")
    objects_list = []
    for task in tasks:
        task = classes.Task(task[1],task[2],task[3],task[4])
        objects_list.append(task)
    return objects_list
             
def load(user_id):
    tasks = get_dicts(user_id)
    today_tasks = []
    for task in tasks:
        if task['date'] == str(date.today()):
            today_tasks.append(task)
    return today_tasks

def save(tasks_list:list):
    query_db(f"DELETE FROM tasks")
    for task in tasks_list:
        if task.date >= str(date.today()):
            query_db(f"INSERT INTO tasks(user_id,category,description,date) VALUES('{task.user_id}','{task.category}','{task.description}','{task.date}')")

def save_user(users_list:list):
    query_db(f"DELETE FROM users")
    for user in users_list:
        query_db(f"INSERT INTO users(username,password) VALUES('{user.username}','{user.password}')")

def get_task_id(user_id="",category="", description="", date=""):
    return query_db(f"SELECT id FROM tasks WHERE description='{description}' AND user_id='{user_id}' AND category='{category}' AND date='{date}'")

def save_add(task):
    task = classes.Task(user_id=task.user_id, category=task.category, description=task.description, date=task.date)
    if task.date >= str(date.today()):
        query_db(f"INSERT INTO tasks(user_id,category,description,date) VALUES('{task.user_id}','{task.category}','{task.description}','{task.date}')")

def save_delete(task):
    task = classes.Task(user_id=task.user_id, category=task.category, description=task.description, date=task.date)
    query_db(f"DELETE FROM tasks WHERE (user_id,category,description,date)=('{task.user_id}','{task.category}','{task.description}','{task.date}')")

def save_new_update(task):
    task = classes.Task(user_id=task.user_id, category=task.category, description=task.description, date=task.date)
    task_id=get_task_id(user_id=task.user_id, category=task.category, description=task.description, date=task.date)
    tasks=get_dicts(task.user_id)
    for task in tasks:
        if task_id == task['id']:
            query_db(f"UPDATE tasks SET user_id='{task.user_id}', category='{task.category}', description='{task.description}', date='{task.date}'")


