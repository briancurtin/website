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
