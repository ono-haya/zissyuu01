from flask import Flask, session, render_template, request
import csv
from flask_session import Session
from apps.check_credit_copy import get_credit


app = Flask(__name__)

app.config["SESSION_TYPE"] = "filesystem"
#apps直下にflask_sessionが自動的に作成され、保存される
Session(app)

#ページごとの要素数は20とする
per_page = 20

@app.route("/")
def main(initialize = True):    
    return render_template("home.html")

@app.route("/result", methods=["GET", "POST"])
def get_result():
    #フォームの情報(ファイル、専攻)を取得
    file = request.files.get("file")
    if file is None or file.filename == "":
        return "ファイルが選択されていません", 400
    major = request.form.get("major")
    #専攻の情報をセッションに保存
    session["major"] = major
    #処理を行う
    #マッチングの結果を保存する（不足単位の結果、教科の結果）
    session["currentstate"] = get_credit(file, major)
    session["matchresult"] = [
        ["順位", "科目番号", "科目名", "学期", "時限", "適合度"],  # ←スキーマ行
        ["1", "GE70101", "知識情報システム実習A", "春", "1", "90"],
        ["2", "GE70102", "知識情報システム実習B", "秋", "2", "85"],
        ["3", "GE70103", "知識情報システム実習C", "春", "3", "80"]
    ]
    #処理の結果をセッションに保存
    #結果のビジュアルを呼び出す
    return show_result()

#キャッシュ内にあるデータを取得して結果画面を表示する
@app.route("/result/<int:current_page>")
def show_result():
    print("セッションの中身", session["currentstate"])
    resutList = session["matchresult"]
    resultHTML = ""
    for i in range(len(resutList)):
        if i == 0:
            resultHTML += "<tr>" + "".join(f"<th>{attr}</th>" for attr in resutList[i]) + "</tr>"
        else:
            resultHTML += "<tr>" + "".join(f"<td>{attr}</td>" for attr in resutList[i]) + "</tr>"
    
    #返ってきた結果を表示できる状態にする
    for i in range(per_page):
        continue
    
    return render_template("result.html",major = session["major"], currentstate = session["currentstate"], matchresult = resultHTML)

#引数のCSVをデータ処理部分に送る

#帰ってきた配列を用いて結果の表示をする
