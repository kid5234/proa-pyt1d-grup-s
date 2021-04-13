def hitung_rekreasi(tiket=0, pgj=0, persen=0):
    pengunjung = int(pgj)
    persentase = int(persen)/100
    htm = int(tiket)
    if htm != 0:
        result = htm * 0.0013 * pengunjung * 300 * persentase
    else:
        result = 6000000
    return result


def Hotel(kmr):
    kamar = int(kmr)
    if kamar == 0:
        result = 1600000
    elif kamar <= 50:
        result = 2000000
    elif kamar <= 100:
        result = 4000000
    elif kamar <= 150:
        result = 6000000
    elif kamar <= 200:
        result = 8000000
    else:
        result = 12000000
    return result


def karaoke(aula, klg, ex, kubus, hk):
    result = {}
    ruangAula = int(aula)
    ruangKeluarga = int(klg)
    ruangEksekutif = int(ex)
    ruangKubus = int(kubus)
    hari_kerja = int(hk)
    pencipta = ((ruangAula*20000*hari_kerja)+(ruangKeluarga*12000*hari_kerja)+(ruangEksekutif*50000*hari_kerja))*0.5+(ruangKubus*300000)
    terkait = ((ruangAula*20000*hari_kerja)+(ruangKeluarga*12000*hari_kerja)+(ruangEksekutif*50000*hari_kerja))*0.5+(ruangKubus*300000)
    # result['pencipta'] = pencipta
    # result['terkait'] = terkait
    result = pencipta + terkait
    return result


def resto(krs):
    kursi = int(krs)
    royalti = 60000 * kursi
    return royalti


def pub(lruang):
    luas = int(lruang)
    royalti = 180000 * luas
    return royalti


def disko(lruang):
    luas = int(lruang)
    royalti_pencipta = 250000 * luas
    royalti_hak_terkait = 180000 * luas
    return royalti_hak_terkait, royalti_pencipta


def nada(nsp):
    sambungan = int(nsp)
    royalti = sambungan * 100000
    return royalti


def bank(lbank):
    luas = int(lbank)
    royalti = luas * 6000
    return royalti


def bioskop():
    layar = int(input("Jumlah layar : "))
    royalti = layar * 3600000
    return royalti


def pameran():
    royalti = 1500000
    return royalti


def pesawatinflight(pnmpang, tkt, dur):
    penumpang = int(pnmpang)
    tiket = int(tkt)
    durasi = int(dur)
    royalti = penumpang * 0.25 * 0.01 * tiket * 10 * 0.01 * durasi
    return royalti


def pesawatonground(hrgtiket, dur):
    tiket = int(hrgtiket)
    durasi = int(dur)
    royalti = 0.25 * 0.01 * tiket * durasi
    return royalti


def kereta(pnmpang, tkt, dur):
    penumpang = int(pnmpang)
    tiket = int(tkt)
    durasi = int(dur)
    royalti = penumpang * 0.25 * 0.01 * tiket * 10 * 0.01 * durasi
    return royalti


def Mall(lruang):
    ruang = int(lruang)
    if ruang >= 500:
        ruang -= 500
        royalti = 4000 * 500
        if ruang >= 500:
            ruang -= 500
            royalti += 3500*500
            if ruang >= 1000:
                ruang -= 1000
                royalti += 3000*1000
                if ruang >= 3000:
                    ruang -= 3000
                    royalti += 2500*3000
                    if ruang >= 5000:
                        ruang -= 5000
                        royalti += 2000*5000
                        if ruang >= 5000:
                            ruang -= 5000
                            royalti += 1500*5000
                            if ruang >= 0:
                                royalti += 1000*1000
                        else:
                            royalti += 1500*ruang
                    else:
                        royalti += 2000 * ruang
                else:
                    royalti += 2500*ruang
            else:
                royalti += 3000*ruang
        else:
            royalti += 3500*ruang
    else:
        royalti = 4000 * ruang
    return royalti
