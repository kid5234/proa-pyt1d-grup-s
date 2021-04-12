from flask import Flask, render_template, request, jsonify

from app import app
import app.royalti as r

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


@app.route('/proseshitung')
def proseshitung():
    cat = request.args.get("cat")
    kmrhotel = request.args.get("kmrhotel")
    print(cat)
    bayar = r.Hotel(kmrhotel)
    print(bayar)
    try:
        return jsonify(result="{:,}".format(bayar))
    except Exception as e:
        return str(e)
