from flask import Flask, render_template

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
