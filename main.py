from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todolist = [{'task': 'lavar o chao', 'status': True}]

@app.route('/')
def home():
    item_count = len(todolist) 
    return render_template('index.html', todos=todolist, count=item_count)


@app.route('/add', methods=['POST'])
def add():
    new_todo = request.form['task']
    todolist.append({"task": new_todo, "status": False})
    return redirect(url_for('home'))


@app.route('/toggle/<int:task_index>', methods=['POST'])
def toggle(task_index):
    todolist[task_index]['status'] = not todolist[task_index]['status']
    return redirect(url_for('home'))


@app.route('/delete_task/<int:task_index>', methods=['POST'])
def delete_task(task_index):
    todolist.pop(task_index) 
    return redirect(url_for('home'))


@app.route('/delete-all', methods=['POST'])
def delete_all():
    todolist.clear()
    return redirect(url_for('home'))


app.run(debug=True)