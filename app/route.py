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
    try:
        cat = request.args.get("cat")
        print(cat)
        if cat == 'rekreasi':
            tiket = request.args.get("htm")
            pgj = request.args.get("pengunjung")
            persen = request.args.get("persentase")
            bayar = r.hitung_rekreasi(tiket, pgj, persen)
            print(bayar)
        elif cat == 'hotel':
            kmrhotel = request.args.get("kmrhotel")
            bayar = r.Hotel(kmrhotel)
        elif cat == 'konser':
            bayar = 0
        elif cat == 'karaoke':
            aula = request.args.get("raula")
            klg = request.args.get("rklg")
            ex = request.args.get("rex")
            kubus = request.args.get("rkubus")
            hk = request.args.get("hkerja")
            bayar = r.karaoke(aula, klg, ex, kubus, hk)
            print(aula, klg, ex, kubus, hk, bayar)
        elif cat == 'maldsb':
            lruang = request.args.get("lmall")
            bayar = r.Mall(lruang)
        elif cat == 'restokafe':
            kursi = request.args.get("jmlkur")
            bayar = r.resto(kursi)
        elif cat == 'pubbar':
            lruang = request.args.get("lpub")
            bayar = r.pub(lruang)
        elif cat == 'diskotik':
            lruang = request.args.get("ldisk")
            bayar = r.disko(lruang)
        else:
            pass

        print(bayar)
        return jsonify(result="{:,}".format(bayar))
    except Exception as e:
        return str(e)
