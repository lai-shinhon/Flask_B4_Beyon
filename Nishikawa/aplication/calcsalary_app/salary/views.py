
from flask import request, redirect, url_for, render_template, flash, session
from salary import app


@app.route('/')
def show_entries():
        return render_template("input.html")

@app.route('/output', methods=['GET', 'POST'])
def outputSalary():
        
        input_salary = int(request.form["salary"])
        if input_salary <= 1000000:
            tax=round(input_salary*0.1)
        else:
            tax=round((input_salary-1000000)*0.2+100000)

        pay=input_salary-tax

        return render_template("output.html", salary=f"給与:{input_salary}、支給額:{pay}、税額:{tax}")