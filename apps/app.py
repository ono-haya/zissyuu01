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
    #マッチングの結果を保存する（不足単位の結果、教科の結果）
    session["currentstate"] 

    #session["makegame"]
    #処理の結果をセッションに保存
    #結果のビジュアルを呼び出す
    return show_result()

#キャッシュ内にあるデータを取得して結果画面を表示する
@app.route("/result/<int:current_page>")
def show_result():
    #この数字はサンプル
    total = 84
    
    
    return render_template("result.html",major = session["major"], currentstatus = session["currentstate"] )

#引数のCSVをデータ処理部分に送る

#帰ってきた配列を用いて結果の表示をする
