from flask import request, redirect, url_for, render_template, flash, session
from salary import app


@app.route('/')
def show_entries():
    return render_template('input.html')


@app.route('/output', methods=['GET', 'POST'])
def salaryout():
    input_salary = int(request.form['salary'])

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