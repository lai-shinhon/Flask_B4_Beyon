from flask import request, redirect, url_for, render_template, flash, session
from salary import app

@app.route('/', methods=['GET', 'POST'])
def show_entries():
    input_data = session.get('input_data', None)
    return render_template('input.html', input = input_data)
    # return render_template('input.html')

@app.route('/output', methods=['GET', 'POST'])
def outputSalary():

    input_salary = int(request.form['salary'])
    tax = 0
    if input_salary > 1000000:
        # 100万を超えるときの税金を計算する
        tax = round((input_salary-1000000)*0.2 + 1000000*0.1)
    else:
        # 100万以下の税金を計算する
        tax = round(input_salary*0.1)

    # return f"給与:{input_salary}、支給額:{input_salary-tax}、税額:{tax}"
    return render_template('output.html', salary=f"給与:{input_salary}、支給額:{input_salary-tax}、税額:{tax}")

@app.route('/profile')
def profilePage():
    return "Here is Profile"