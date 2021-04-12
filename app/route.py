from flask import render_template

from app import app

# from app import royalti


@app.route('/')
def index():
    return render_template("home.html", title='- Home')


@app.route('/about')
def about():
    return render_template("howto.html", title='- Tutorial')


@app.route('/hitung')
def hitung():
    return render_template("calculate.html", title='- Kalkulasi')
