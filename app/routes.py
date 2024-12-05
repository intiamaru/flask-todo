from flask import render_template, request, jsonify, redirect, url_for
from app import app, db
from app.models import Todo

@app.route('/')
def index():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return render_template('index.html', todos=todos)

@app.route('/add_todo', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    description = request.form.get('description')
    
    if title:
        todo = Todo(title=title, description=description)
        db.session.add(todo)
        db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/toggle_todo/<int:todo_id>')
def toggle_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete_todo/<int:todo_id>')
def delete_todo(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))
