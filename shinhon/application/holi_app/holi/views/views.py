from flask import request, redirect, url_for, render_template, flash, session
from holi import app, db
from holi.models.entries import Entry

@app.route('/', methods=["GET", "POST"])
def show_entries():
    return render_template('entries.html')

@app.route('/maintenance_date', methods=["GET"])
def show_maintenance():
    database_state = session.get('state', None)
    return render_template('maintenance.html', state=database_state)

@app.route('/list', methods=["GET"])
def show_list():
    holidays = Entry.query.all()
    print(f"list: {show_list}")
    return render_template('list.html', holidays=holidays)
