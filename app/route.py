from flask import Flask, render_template, request, jsonify

from app import app
import app.royalti as r
import app.forms as f

# from app import royalti


# route to Home
@app.route('/')
def index():
    return render_template("home.html", title='')


# route to tutorial
@app.route('/about')
def about():
    return render_template("howto.html", title='- Tutorial')


# route to kalkulasi
@app.route('/hitung')
def hitung():
    catForm = f.JenisForm()
    return render_template(
        "calculate.html",
        title='- Kalkulasi',
        catForm=catForm
    )


# background prosess untuk perhitungan
@app.route('/proseshitung')
def proseshitung():
    try:
        cat = request.args.get("cat")
        print(cat)  # cek kategori
        if cat == 'rekreasi':
            tiket = request.args.get("htm")
            pgj = request.args.get("pengunjung")
            persen = request.args.get("persentase")
            bayar = r.hitung_rekreasi(tiket, pgj, persen)
        elif cat == 'hotel':
            kmrhotel = request.args.get("kmrhotel")
            bayar = r.Hotel(kmrhotel)
        elif cat == 'konser':
            gross = request.args.get("tiketkotor")
            free = request.args.get("tiketgratis")
            bproduk = request.args.get("biayaprod")
            bayar = r.hitung_konser(gross, free, bproduk)
        elif cat == 'karaoke':
            aula = request.args.get("raula")
            klg = request.args.get("rklg")
            ex = request.args.get("rex")
            kubus = request.args.get("rkubus")
            hk = request.args.get("hkerja")
            bayar = r.karaoke(aula, klg, ex, kubus, hk)
        elif cat == 'maldsb':
            lruang = request.args.get("lmall")
            bayar = r.Mall(lruang)
        elif cat == 'restokafe':
            krs = request.args.get("jmlkur")
            bayar = r.resto(krs)
        elif cat == 'pubbar':
            lruang = request.args.get("lpub")
            bayar = r.pub(lruang)
        elif cat == 'diskotik':
            lruang = request.args.get("ldisk")
            bayar = r.disko(lruang)
        else:
            pass
        print(bayar)  # cek isinya
        return jsonify(result="{:,}".format(bayar))
    except Exception as e:
        return str(e)
