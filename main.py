from flask import Flask, render_template, request, redirect, url_for
from config import Task, db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todolist.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def home():
    tasks = Task.query.all()
    item_count = len(tasks) 
    return render_template('index.html', todos=tasks, count=item_count)


@app.route('/add', methods=['POST'])
def add():
    new_todo = request.form['task']
    tasks = Task(task=new_todo, status=False)
    db.session.add(tasks)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/toggle/<int:task_id>', methods=['POST'])
def toggle(task_id):
    tasks = Task.query.get(task_id)
    tasks.status = not tasks.status
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    tasks = Task.query.get(task_id)
    db.session.delete(tasks)
    db.session.commit()
    return redirect(url_for('home'))


@app.route('/delete-all', methods=['POST'])
def delete_all():
    db.session.query(Task).delete()
    db.session.commit()
    return redirect(url_for('home'))

with app.app_context():
    db.create_all()