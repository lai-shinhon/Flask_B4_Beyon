
from flask import request, redirect, url_for, render_template, flash, session
from salary import app


@app.route('/')
def show_entries():
        return render_template("input.html")

@app.route('/output', methods=['GET', 'POST'])
def outputSalary():
        
        salary_output = None

        if request.form["salary"] != "":
              
              #formに入力されている数値を取得
              input_salary = int(request.form["salary"])
              print(f"入力した数値:{input_salary}")
              
              #税金を保存するための変数を宣言
              tax=0

              #sessionに入力した数値を保存する
              session["input_data"]=input_salary

              if request.method == "POST":
                    if input_salary > 1000000:
                          #100万円を超えるときの税金を計算
                          tax = round((input_salary-1000000)*0.2 + 1000000*0.1)
                    else:
                          #100万円以下の税金を計算する
                          tax = round(input_salary*0.1)
              salary_output = f"給与":

        pay=input_salary-tax

        return render_template("output.html", salary=f"給与:{input_salary}、支給額:{pay}、税額:{tax}")