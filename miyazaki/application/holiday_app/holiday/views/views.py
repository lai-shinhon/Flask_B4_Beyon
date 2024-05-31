from flask import request, redirect, url_for, render_template, flash, session
from holiday import app
from holiday import db
from holiday.models.holidays import Holiday



@app.route('/')
def index_page():
    return render_template('holidays/input.html')


@app.route('/result', methods=['POST'])
def result_page():
    h_day = request.form['holiday_date']
    h_text = request.form['holiday_text']
    if request.form['button'] == "insert_update":
        # 新規登録、更新
        if Holiday.query.get(h_day) is None:
            holiday = Holiday(
                holi_date = h_day,
                holi_text = h_text
            )
            db.session.merge(holiday)
            db.session.commit()
            result_day = f"{h_day}（{h_text}）が登録されました"
            flash('新しく祝日が登録されました')
            return render_template('holidays/result.html', result_day = result_day)
        else:
            holiday = Holiday.query.get(h_day)
            holiday.holi_text = h_text
            db.session.merge(holiday)
            db.session.commit()
            result_day = f"{h_day}（{h_text}）が登録されました"
            flash('祝日が更新されました')
            return render_template('holidays/result.html', result_day = result_day)
    elif request.form['button'] == "delete":
        # 削除
        if Holiday.query.get(h_day) is None:
            result_day = f"{h_day}は祝日マスタに登録されていません"
            flash(f'{result_day}')
            return redirect(url_for('index_page'))
        else:
            holiday = Holiday.query.get(h_day)
            h_text_d = holiday.holi_text
            db.session.delete(holiday)
            db.session.commit()
            flash('祝日が削除されました')
            result_day = f"{h_day}（{h_text_d}）は削除されました"
            return render_template('holidays/result.html', result_day = result_day)


@app.route('/list', methods=['POST'])
def list_page():
    holidays = Holiday.query.order_by(Holiday.holi_date.asc()).all()
    return render_template('holidays/list.html', holidays = holidays)