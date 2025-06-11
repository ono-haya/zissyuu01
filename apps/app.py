from flask import Flask, session, render_template, request
import csv
from flask_session import Session
from apps.check_credit_copy import get_credit
from apps.classinfomanager import get_classinfo
from apps.suisen import get_suisen
import io


app = Flask(__name__)

app.config["SESSION_TYPE"] = "filesystem"
#apps直下にflask_sessionが自動的に作成され、保存される
Session(app)

element_amount = 3


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


    credits =  get_credit(file, major)
    file.stream.seek(0)
    ranking = get_suisen(file, major)

    #マッチングの結果を保存する（不足単位の結果、教科の結果）
    session["currentstate"] = credits[0]
    session["main_prefix"] = credits[1]
    session["other_prefix"] = credits[2]
    session["matchresult"] = get_classinfo(ranking)

    #処理の結果をセッションに保存
    #結果のビジュアルを呼び出す
    return show_result()

#キャッシュ内にあるデータを取得して結果画面を表示する
@app.route("/result/<int:current_page>")
def show_result():
    print("セッションの中身", session["currentstate"])
    resutLists = session["matchresult"]
    resultHTML = ""
    for list in resutLists:
        resultHTML +="<table>"
        #HTML要素に変換する(最初の要素はラベル)
        for i in range(element_amount+1):
            if i == 0:
                resultHTML += "<tr>" + "".join(f"<th>{attr}</th>" for attr in list[i]) + "</tr>"
            else:
                resultHTML += "<tr>" + "".join(f"<td>{attr}</td>" for attr in list[i]) + "</tr>"
        resultHTML += "</table>"
    
    #専攻内、専攻外の科目番号のプレフィックスを取得し、HTML対応の文字列に変換する
    main_prefix = session["main_prefix"]
    other_prefix = ",".join(f"{p}" for p in session["other_prefix"]) 
     

    #返ってきた結果を表示できる状態にする
    for i in range(element_amount):
        continue
    
    return render_template("result.html",major = session["major"], currentstate = session["currentstate"], matchresult = resultHTML, mainPrefix = main_prefix, otherPrefix = other_prefix)

