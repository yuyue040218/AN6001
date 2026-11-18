# web app

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    q = request.form.get("q")
    return(render_template("index.html"))

@app.route("/main", methods=["GET","POST"])
def main():
    # q = request.form.get("q")
    return(render_template("main.html"))

@app.route("/dbs", methods=["GET","POST"])
def dbs():
    return(render_template("dbs.html"))

@app.route("/dbsPred", methods=["GET","POST"])
def dbsPred():
    return(render_template("dbsPred.html"))

if __name__ == "__main__":
    app.run()