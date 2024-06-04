from flask import request, redirect, url_for, render_template, flash, session
from ballon import app, db
from ballon.models.entries import Entry
import random

@app.route('/', methods=["GET", "POST"])
def show_entries():
    return render_template("entries.html")

@app.route('/result/<int:id>', methods=["GET"])
def show_result(id):
    entry = Entry.query.get(id)
    # print(f"haha{result}")
    return render_template("result.html", entry=entry)

@app.route('/list', methods=["GET"])
def show_list():
    messages = Entry.query.all()
    print(f"list: {show_list}")
    return render_template('list.html', messages=messages)

@app.route('/ready', methods=["POST"])
def prepare_ready():
    input_message = request.form['message']
    input_air = int(request.form['input_air'])
    ballon_size = random.randint(10, 100)

    entry = Entry(
        size = ballon_size,
        air = input_air,
        message = input_message,
        country = None
    )

    db.session.add(entry)
    db.session.commit()

    data = Entry.query.get(entry.id)
    print(f"list: {data}")

    session['result'] = str(data)
    # print(f"result: {input_message}/{input_air}/{ballon_size}")
    return redirect(url_for('show_result', id=entry.id))
