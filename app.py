from flask import Flask, session, render_template, redirect, url_for, request
app = Flask(__name__)
import db
import functions
from datetime import timedelta
import datetime

app.secret_key = "sekflbskgvjd"
app.permanent_session_lifetime = timedelta(days=11)

@app.route('/')
def home():
    if session.get("user_id", "")=="":
        return render_template("login.html")
    return redirect("/today")

@app.route('/login', methods=['GET','POST'])
def login():
    username=request.form["username"]
    password=request.form["password"]
    if db.login(username, password):
        user_id=db.get_user_id(username)
        session.permanent = True
        session["user_id"]=user_id
        return redirect("/today")
    else:
        return render_template("login.html")

@app.route('/today')
def today():
    if "user_id" in session:
        user_id = session['user_id']
        today=datetime.date.today()
        today_tasks=db.load(user_id)
        sorted_list = sorted(today_tasks, key=lambda d: d['category'])
        return render_template("today.html", sorted_list=sorted_list, day=today.day, month=today.month, year=today.year)
    else:
         return render_template("login.html")
    
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
    if "user_id" in session:
        user_id = session['user_id']
        tasks = db.get_objects(user_id)
        db.save(tasks)
        session.pop('user_id', None)
        return render_template("login.html")

@app.route('/add')
def add():
    if "user_id" in session:
        user_id = session['user_id']
        category = request.args["category"]
        description = request.args["description"]
        date = request.args["date"]
        functions.add(user_id=user_id, category=category, description=description, date=date)
        today=datetime.date.today()
        today_tasks=db.load(user_id)
        sorted_list = sorted(today_tasks, key=lambda d: d['category'])
        return render_template("today.html", sorted_list=sorted_list, day=today.day, month=today.month, year=today.year)
    else:
        return render_template("login.html")

@app.route('/delete')
def delete(user_id):
    session["user_id"]=user_id
    category = request.args["category"]
    description = request.args["description"]
    date = request.args["date"]
    functions.delete(user_id=user_id, category=category, description=description, date=date)
    return redirect(f"/Tasks_List")

@app.route('/update')
def update(user_id):
    session["user_id"]=user_id
    category = request.args["category"]
    description = request.args["description"]
    date = request.args["date"]
    functions.update(user_id=user_id, category=category, description=description, date=date)
    return redirect(f"/Tasks_List")

@app.route('/to_update')
def to_update(user_id):
    session["user_id"]=user_id
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
def tasks_list():
    if "user_id" in session:
        user_id = session['user_id']
        tasks = db.get_dicts(user_id)
        new_tasks = []
        for task in tasks:
            if task['date'] >= str(datetime.date.today()):
                new_tasks.append(task)
        sorted_list = sorted(new_tasks, key=lambda elem: "%s %s" % (elem['date'], elem['category']))
        return render_template("Tasks_List.html", sorted_list=sorted_list)
    else:
        return render_template("login.html")
        

if __name__ == '__main__':
    app.run(debug=True)

