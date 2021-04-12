def hitung_rekreasi(htm, pgj, persen):
    pengunjung = int(pgj)
    persentase = float(persen/100)
    if htm != 0:
        result = htm * 0.0013 * pengunjung * 300 * persentase
        print('Total biaya royalti musik dalam satu tahun adalah Rp', result)
    else:
        result = 6000000
        print('Total biaya royalti musik dalam satu tahun adalah Rp', result)
    return result


def Hotel(kmr):
    kamar = int(kmr)
    if kamar == 0:
        royalti = 1600000
    elif kamar <= 50:
        royalti = 2000000
    elif kamar <= 100:
        royalti = 4000000
    elif kamar <= 150:
        royalti = 6000000
    elif kamar <= 200:
        royalti = 8000000
    else:
        royalti = 12000000
    return royalti
