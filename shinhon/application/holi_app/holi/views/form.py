from flask import request, redirect, url_for, render_template, flash, session
from holi import app, db
from holi.models.entries import Entry

@app.route('/check_update', methods=["POST"])
def check_update():
    if request.form['holiday']:
        # 入力した日付を取得する
        input_date = request.form['holiday']
        input_text = request.form['holiday_text']
        # データベースが入力した日付の祝日があるかどうかを確認
        has_Entry = Entry.query.filter_by(holi_date=input_date).first()

        if request.form['button'] == 'insert_update':
            # 「新規登録・更新」ボタンが押されたときの処理
            session['state'] = ''

            # 更新するデータの内容を用意する
            entry = Entry(
                holi_date = input_date,
                holi_text = input_text
            )

            if has_Entry:
                # 既存のデータを更新する
                db.session.merge(entry)
                # 処理結果のテキストをsessionに登録する
                session['state'] = f"{input_date}は「{input_text}」に更新されました"
            else:
                # 新規データを追加する
                db.session.add(entry)
                # 処理結果のテキストをsessionに登録する
                session['state'] = f"{input_date}（{input_text}）が登録されました"
        elif request.form['button'] == 'delete':
            # 「削除」ボタンが押されたときの処理
            if has_Entry:
                db.session.delete(has_Entry)
                # 処理結果のテキストをsessionに登録する
                session['state'] = f"{has_Entry.holi_date}（{has_Entry.holi_text}）は、削除されました"
            else:
                flash(f"{input_date}は、祝日マスタに登録されていません", 'danger')
                return redirect(url_for('show_entries'))
        db.session.commit()
        return redirect(url_for('show_maintenance'))
    else:
        flash("日付を指定してください")
        return redirect(url_for('show_entries'))
