from flask import render_template

from app import app

@app.route('/')
@app.route('/<name>')
def render(name="index"):
    return render_template("%s.html" % name)
