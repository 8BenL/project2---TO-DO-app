from flask import Flask, session, render_template, redirect, request
app = Flask(__name__)
import db
import functions
from datetime import timedelta
import datetime
import classes


app.secret_key = "sekflbskgvjd"
app.permanent_session_lifetime = timedelta(days=11)


@app.route('/')
def home():
    if session.get("user_id", "")=="":
        return render_template("login.html")
    return redirect("/today")

@app.route('/login', methods=['GET','POST'])
def login():
    username=request.form.get("username",None)
    password=request.form.get("password",None)
    if username is None or password is None:
        return redirect("/logout")
    if db.login(username=username, password=password):
        user_id=db.get_user_id(username=username, password=password)
        session.permanent = True
        session["user_id"] = user_id
        return redirect("/today")
    else:
        return redirect('/logout')

    
@app.route('/today')
def today():
    if "user_id" in session:
        user_id = session['user_id']
        username = db.get_username(user_id)
        today=datetime.date.today()
        today_tasks=db.load(user_id)
        sorted_list = sorted(today_tasks, key=lambda d: d['category'])
        return render_template("today.html", username=username, sorted_list=sorted_list, day=today.day, month=today.month, year=today.year)
    else:
         return render_template("login.html")
    
@app.route('/sign_up', methods=['GET','POST'])
def sign_up():
    username=request.form.get('username',None)
    password=request.form.get('password',None)
    if username is None or password is None:
        return render_template("sign_up.html")
    users_list = db.users_list()
    new_user = classes.User(username=username, password=password)     
    users_list.append(new_user)
    db.save_user(users_list)
    return render_template("login.html") 

@app.route('/to_sign_up')
def to_sign_up():
    return render_template("sign_up.html")

@app.route('/logout')
def logout():
    if "user_id" in session:
        session.pop('user_id', None)
        return redirect("/")
    else:
        return redirect("/")

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
        username=db.get_username(user_id)
        sorted_list = sorted(today_tasks, key=lambda d: d['category'])
        return render_template("today.html", username=username, sorted_list=sorted_list, day=today.day, month=today.month, year=today.year)
    else:
        return render_template("login.html")

@app.route('/add_Task_list')
def add_Task_list():
    if "user_id" in session:
        user_id = session['user_id']
        category = request.args["category"]
        description = request.args["description"]
        date = request.args["date"]
        functions.add(user_id=user_id, category=category, description=description, date=date)
        username = db.get_username(user_id)
        tasks = db.get_dicts(user_id)
        new_tasks = []
        for task in tasks:
            if task['date'] >= str(datetime.date.today()):
                new_tasks.append(task)
        sorted_list = sorted(new_tasks, key=lambda elem: "%s %s" % (elem['date'], elem['category']))
        return render_template("Tasks_List.html", username=username, sorted_list=sorted_list)
    else:
        return render_template("login.html")

@app.route('/delete')
def delete():
    if "user_id" in session:
        user_id = session['user_id']
        category = request.args["category"]
        description = request.args["description"]
        date = request.args["date"]
        functions.delete(user_id=user_id, category=category, description=description, date=date)
        return redirect(f"/Tasks_List")
    else:
        return render_template("login.html")

@app.route('/delete_today')
def delete_today():
    if "user_id" in session:
        user_id = session['user_id']
        category = request.args["category"]
        description = request.args["description"]
        date = request.args["date"]
        functions.delete(user_id=user_id, category=category, description=description, date=date)
        today=datetime.date.today()
        today_tasks=db.load(user_id)
        username=db.get_username(user_id)
        sorted_list = sorted(today_tasks, key=lambda d: d['category'])
        return render_template("today.html", username=username, sorted_list=sorted_list, day=today.day, month=today.month, year=today.year)
    else:
        return render_template("login.html")

@app.route('/update/<id>')
def update(id: str):
    if "user_id" in session:
        user_id = session['user_id']
        category = request.args["category"]
        description = request.args["description"]
        date = request.args["date"]
        updated = functions.update(task_id=id, user_id=user_id, category=category, description=description, date=date)
        print(updated)
        return redirect(f"/Tasks_List")
    else:
        return render_template("login.html")


@app.route('/completed_today/<task_id>/')
def completed_today(task_id: int):
    completed = request.args["completed"]
    functions.toggle_task(task_id=task_id, completed=completed)
    return redirect("/today")

@app.route('/to_update')
def to_update():
    if "user_id" in session:
        task_id = request.args['id']
        user_id = session['user_id']
        category = request.args["category"]
        description = request.args["description"]
        date = request.args["date"]
        return render_template("update.html", id=task_id, user_id=user_id, category=category, description=description, date=date)
    else:
        return render_template("login.html")

@app.route('/search')
def search():
     if "user_id" in session:
        user_id = session['user_id']
        query = request.args["query"]
        results = functions.search(user_id=user_id, query=query)
        return render_template("Tasks_List.html", sorted_list=results)
     else:
        return render_template("login.html")

@app.route('/Tasks_List')
def tasks_list():
    if "user_id" in session:
        user_id = session['user_id']
        username = db.get_username(user_id)
        tasks = db.get_dicts(user_id)
        new_tasks = []
        for task in tasks:
            if task['date'] >= str(datetime.date.today()):
                new_tasks.append(task)
        sorted_list = sorted(new_tasks, key=lambda elem: "%s %s" % (elem['date'], elem['category']))
        return render_template("Tasks_List.html", username=username, sorted_list=sorted_list)
    else:
        return render_template("login.html")

@app.route('/api/tasks_board', methods=['GET'])
def tasks_board():
      if "user_id" in session:
        user_id = session['user_id']
        return list(filter(lambda task_dict: task_dict['completed'] == 0 , db.load(user_id)))
       
@app.route('/api/completed_board', methods=['GET'])
def completed_board():
      if "user_id" in session:
        user_id = session['user_id']
        return list(filter(lambda task_dict: task_dict['completed'] == 1 , db.load(user_id)))

@app.route('/api/sign_up', methods=['GET'])
def users_list():
        return db.users_list()        
        
if __name__ == '__main__':
    app.run(debug=True)
    

