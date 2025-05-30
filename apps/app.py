from flask import Flask, session, render_template, request
import csv
from flask_session import Session

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
    major = request.form.get("major")
    #専攻の情報をセッションに保存
    session["major"] = major
    #処理を行う
    #処理の結果をセッションに保存
    
    return show_result()

#キャッシュ内にあるデータを取得して結果画面を表示する
@app.route("/result/<int:current_page>")
def show_result(current_page = 1):
    #この数字はサンプル
    total = 84
    
    total_pages = (total + per_page - 1) // per_page
    index_start = (current_page - 1) * per_page
    index_end = index_start + per_page
    return render_template("result.html",
                           current_page=current_page,
                           total_pages=total_pages,
                           total=total)

#引数のCSVをデータ処理部分に送る

#帰ってきた配列を用いて結果の表示をする
