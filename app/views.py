from flask import render_template

from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/photography/<name>')
def photography(name="baseball"):
    return render_template("%s.html" % name)

@app.route("/photography/thag-20170630")
def thag_20170630():
    return render_template("thag-20170630.html")
