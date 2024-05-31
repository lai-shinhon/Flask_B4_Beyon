from flask import request, redirect, url_for, render_template, flash, session
from salary import app


@app.route('/')
def show_entries():
    input_data = session.get("data", None)
    return render_template('input.html', input = input_data)


@app.route('/output', methods=['GET', 'POST'])
def salaryout():

    if request.method == 'POST':
        input_salary = int(request.form['salary'])
        
        if input_salary is None:
                flash("給与が未入力です。入力してください。")
                return redirect(url_for("show_entries"))
            
        elif  9999999999 < input_salary:
                flash("給与には最大9,999,999,999まで入力可能です。")
                session["data"] = str(input_salary)
                return redirect(url_for("show_entries"))
            
        elif input_salary < 0:
                flash("給与にはマイナスの値は入力できません。")
                session["data"] = str(input_salary)
                return redirect(url_for("show_entries"))
    

        tax_amount = 0.0
        amount_paid = 0.0

        if (input_salary > 1000000):
            tax_amount = round((input_salary - 1000000) * 0.2 + 100000)
            amount_paid = input_salary - tax_amount
        else:
            tax_amount = round(input_salary * 0.1)
            amount_paid = input_salary - tax_amount

        result_salary = "{:,}".format(input_salary)
        result_amount_paid = "{:,}".format(amount_paid)
        result_tax_amount = "{:,}".format(tax_amount)

        return render_template('output.html', salary = f"給与：{result_salary}円の場合、支給額：{result_amount_paid}円、税額：{result_tax_amount}円です。")