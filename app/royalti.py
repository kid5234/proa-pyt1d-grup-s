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


def karaoke():
	ruangAula = int(input('Jumlah ruang karaoke berbentuk Aula: '))
	ruangKeluarga = int(input('Jumlah ruang karaoke berbentuk Karaoke Keluarga: '))
	ruangEksekutif = int(input('Jumlah ruang karaoke berbentuk Karaoke Eksekutif: '))
	ruangKubus = int(input('Jumlah ruang karaoke berbentuk Kubus atau Booth: '))
	hari_kerja = int(input('Jumlah hari beroperasi dalam satu tahun: '))
	pencipta = int(((ruangAula*20000*hari_kerja)+(ruangKeluarga*12000*hari_kerja)+(ruangEksekutif*50000*hari_kerja))*0.5+(ruangKubus*300000))
	terkait = int(((ruangAula*20000*hari_kerja)+(ruangKeluarga*12000*hari_kerja)+(ruangEksekutif*50000*hari_kerja))*0.5+(ruangKubus*300000))
	biaya = int(pencipta+terkait)
	print(f"Biaya Royalti Setahun untuk hak Pencipta adalah Rp {pencipta} dan untuk hak Terkait adalah Rp {terkait} \nTotal keseluruhan biaya royalti setahun adalah Rp {biaya}")

pilih = str(input('Tempat Rekreasi atau Tempat Karaoke? \nMasukkan "r" untuk Rekreasi atau "k" untuk Karaoke: '))
cek = (pilih == 'k') or (pilih == 'r')
while not cek:
	print("!!!!!!"*5)
	print('Mohon masukkan dengan benar!')
	pilih = str(input('Tempat Rekreasi atau Tempat Karaoke? \nMasukkan "r" untuk Rekreasi atau "k" untuk Karaoke: '))
	cek = (pilih == 'k') or (pilih == 'r')
if pilih == 'r':
	hitung_rekreasi()
else:
	karaoke()
