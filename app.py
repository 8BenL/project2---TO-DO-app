from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)
import db
import functions
import datetime


@app.route('/')
def home():
    today=datetime.date.today()
    return render_template("index.html", tasks=db.load(), day=today.day, month=today.month, year=today.year)


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
    return redirect(url_for('home'))

@app.route('/update')
def update():
    category = request.args["category"]
    description = request.args["description"]
    date = request.args["date"]
    functions.update(category=category, description=description, date=date)
    return redirect(url_for('home'))


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
    return render_template("Tasks_List.html", tasks = results)


@app.route('/Tasks_List')
def tasks_list():
    return render_template("Tasks_List.html", tasks=db.get_dicts())
