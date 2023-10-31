from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
import db
import functions
import datetime


@app.route('/')
def home():
    today=datetime.date.today()
    tasks=db.load()
    sorted_list = sorted(tasks, key=lambda d: d['category'])
    return render_template("index.html", sorted_list=sorted_list, day=today.day, month=today.month, year=today.year)


@app.route('/add')
def add():
    category = request.args["category"]
    description = request.args["description"]
    date = request.args["date"]
    functions.add(category=category, description=description, date=date)
    return redirect(url_for('home'))

@app.route('/delete')
def delete():
    category = request.args["category"]
    description = request.args["description"]
    date = request.args["date"]
    functions.delete(category=category, description=description, date=date)
    return redirect("/Tasks_List")

@app.route('/update')
def update():
    category = request.args["category"]
    description = request.args["description"]
    date = request.args["date"]
    functions.update(category=category, description=description, date=date)
    return redirect("/Tasks_List")


@app.route('/to_update')
def to_update(): 
    category = request.args["category"]
    description = request.args["description"]
    date = request.args["date"]
    functions.to_update(category=category, description=description, date=date)
    return render_template("update.html", category=category, description=description, date=date)

@app.route('/search')
def search():
    query = request.args["query"]
    results = functions.search(query=query)
    return render_template("Tasks_List.html", sorted_list=results)


@app.route('/Tasks_List')
def tasks_list():
    tasks = db.get_dicts()
    new_tasks = []
    for task in tasks:
        if task['date'] >= str(datetime.date.today()):
            new_tasks.append(task)
    sorted_list = sorted(new_tasks , key=lambda elem: "%s %s" % (elem['date'], elem['category']))
    return render_template("Tasks_List.html", sorted_list=sorted_list)
        



