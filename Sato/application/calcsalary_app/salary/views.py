from flask import request, redirect, url_for, render_template, flash, session
from salary import app


@app.route('/')
def show_entries():
    return render_template("input.html")

@app.route('/output',methods=['GET','POST'])
def Outputsalary():
    input_salary=int(request.form['salary'])
    tax=0
    if input_salary>1000000:
        tax = 100000 + (input_salary-10000)*0.2
        tax=round(tax)

    else:
        tax = input_salary * 0.1
        tax=round(tax)
        
#支払額計算
    pay=input_salary-tax
    return render_template('output.html',salary=f"給与:{input_salary}、支給額:{pay}、税額: {tax}")

    