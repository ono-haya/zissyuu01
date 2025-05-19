from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "<p>this is app</p>"