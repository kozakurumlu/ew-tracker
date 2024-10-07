from flask import Flask, render_template, request, redirect, url_for, abort
from db import Database  # Assuming your Database class is in db.py
from datetime import datetime

app = Flask(__name__)
db = Database('ew.db')  # Make sure 'ew.db' is in the same directory as app.py

@app.route('/')
def index():
    # Get EWs from the database
    ews = db.get_ews()
    
    # Render the list.html template with the EWs
    return render_template('list.html', ews=ews)

@app.route('/<int:id>')
def ew_detail(id):
    ew = db.get_ew(id)
    if ew is None:
        abort(404)
    return render_template('detail.html', ew=ew)

@app.route('/add', methods=['POST'])
def add_ew():
    task = request.form.get('task')
    subject = request.form.get('subject')
    beak = request.form.get('beak')
    due_date = request.form.get('due_date')
    if task and subject and beak and due_date:
        due_date = datetime.strptime(due_date, '%Y-%m-%d').date()
        db.create_ew(task, subject, beak, due_date)
    return redirect(url_for('index'))

# EXTRA CREDIT
@app.route('/<int:id>')
def view_ew(id):
    """
    TO IMPLEMENT
    """
    pass