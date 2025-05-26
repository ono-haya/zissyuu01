from flask import Flask, render_template
#名前、学籍番号の登録、データの送信、送信データと単位要件の照合(卒業要件、資格要件←トグルで管理？)送信情報の確認　個人情報　ホーム兼登録、送信画面と確認画面で分ける
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("home.html")



@app.route("/test")
def test():
    return "<p>this is app test</p>"

@app.route("/render/<arg>")
def render(arg):
    return ""

