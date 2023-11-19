from flask import Flask, session, render_template, redirect, url_for, request
app = Flask(__name__)
import db
import functions
from datetime import date
import datetime

app.secret_key = "sekflbskgvjd"

@app.route('/')
def home():
    if session.get("user_id", "")=="":
        return render_template("login.html")
    return redirect(f"/today/{session['user_id']}")

@app.route('/login', methods=['POST'])
def login():
    username=request.form["username"]
    password=request.form["password"]
    if db.login(username, password):
        user_id=db.get_user_id(username)
        session["user_id"]=db.get_user_id(username)
        return redirect(f"/today/{user_id}")
    else:
        return render_template("login.html")

@app.route('/today/<user_id>')
def today(user_id=0):
    if session["user_id"]!=int(user_id):
        return logout() 
    today=datetime.date.today()
    today_tasks=db.load(user_id)
    sorted_list = sorted(today_tasks, key=lambda d: d['category'])
    return render_template("today.html", sorted_list=sorted_list, day=today.day, month=today.month, year=today.year)

@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        username=request.form["username"]
        password=request.form["password"]
        functions.sign_up(username, password)
    return render_template("login.html") 

@app.route('/to_sign_up')
def to_sign_up():
    return render_template("sign_up.html")

@app.route('/logout')
def logout():
    user_id=session["user_id"]
    tasks = db.get_objects(user_id)
    db.save(tasks)
    session.pop('user_id', None)
    return redirect(url_for('home'))

@app.route('/add')
def add(user_id=0):
    user_id=session["user_id"]
    category = request.args["category"]
    description = request.args["description"]
    date = request.args["date"]
    functions.add(user_id=user_id, category=category, description=description, date=date)
    today=datetime.date.today()
    today_tasks=db.load(user_id)
    sorted_list = sorted(today_tasks, key=lambda d: d['category'])
    return render_template("today.html", sorted_list=sorted_list, day=today.day, month=today.month, year=today.year)

@app.route('/delete')
def delete(user_id):
    user_id=session["user_id"]
    category = request.args["category"]
    description = request.args["description"]
    date = request.args["date"]
    functions.delete(user_id=user_id, category=category, description=description, date=date)
    return redirect(f"/Tasks_List")

@app.route('/update')
def update(user_id):
    user_id=session["user_id"]
    category = request.args["category"]
    description = request.args["description"]
    date = request.args["date"]
    functions.update(user_id=user_id, category=category, description=description, date=date)
    return redirect(f"/Tasks_List")

@app.route('/to_update')
def to_update(user_id):
    user_id=session["user_id"]
    category = request.args["category"]
    description = request.args["description"]
    date = request.args["date"]
    functions.to_update(user_id=user_id, category=category, description=description, date=date)
    return render_template("update.html", category=category, description=description, date=date)

@app.route('/search')
def search():
    query = request.args["query"]
    results = functions.search(query=query)
    return render_template("Tasks_List.html", sorted_list=results)

@app.route('/Tasks_List')
def tasks_list(user_id=0):
    user_id=session["user_id"]
    tasks = db.get_dicts(user_id)
    new_tasks = []
    for task in tasks:
        if task['date'] >= str(datetime.date.today()):
            new_tasks.append(task)
    sorted_list = sorted(new_tasks, key=lambda elem: "%s %s" % (elem['date'], elem['category']))
    return render_template("Tasks_List.html", sorted_list=sorted_list)
        

if __name__ == '__main__':
    app.run(debug=True)

