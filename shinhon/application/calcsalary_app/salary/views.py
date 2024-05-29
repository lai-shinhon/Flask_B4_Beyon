from flask import request, redirect, url_for, render_template, flash, session
from salary import app

@app.route('/', methods=['GET', 'POST'])
def show_entries():
    # sessionに保存されているinputの記録を呼びだす
    input_data = session.get('input_data', None)
    # print(f"input_data: {input_data}")
    return render_template('input.html', input = input_data)

@app.route('/output', methods=['GET', 'POST'])
def outputSalary():

    salary_output = None

    if request.form['salary'] != '':

        # formに入力されている数値を取得する
        input_salary = int(request.form['salary'])
        print(f"入力した数値の長さ: {len(str(input_salary))}")

        if input_salary > 999999999999:
            flash("最大は999,999,999,999円までです")
            session['input_data'] = ""
        else:
            # 税金を保存するための変数を宣言する
            tax = 0

            # sessionに入力した数値を保存する
            session['input_data'] = input_salary

            if request.method == "POST":
                if input_salary > 1000000:
                    # 100万を超えるときの税金を計算する
                    tax = round((input_salary-1000000)*0.2 + 1000000*0.1)
                else:
                    # 100万以下の税金を計算する
                    tax = round(input_salary*0.1)
            else:
                flash("問題が発生しました！サイトの管理者にお問い合わせしてください")

            # 表示したいテキストを作る
            salary_output = f"給与:{input_salary}、支給額:{input_salary-tax}、税額:{tax}"

    else:
        print(f"input: {type(request.form['salary'])}")
        flash("数値を入力してください")

    return render_template('output.html', salary=salary_output)
