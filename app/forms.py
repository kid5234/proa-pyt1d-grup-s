"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    SelectField,
    RadioField
)
from wtforms.validators import (
    DataRequired,
    ValidationError,
    NumberRange
)


class JenisForm(FlaskForm):
    # untuk kategori jenis usaha
    cat = SelectField(
        'Jenis Usaha',
        choices=[
            ('0', 'Pilih Jenis Usaha'),
            ('rekreasi', 'Pusat Rekreasi'),
            ('konser', 'Konser Musik'),
            ('karaoke', 'Karaoke (Rumah Bernyanyi)'),
            ('restokafe', 'Restaurant dan Kafe'),
            ('pubbar', 'Pub, Bar, dan Bistro'),
            ('maldsb', 'Mall, Supermarket, Toko, Distro, Salon Kecantikan, Pusat Kebugaran, Arena Olahraga, Ruang Pamer'),
            ('hotel', 'Hotel dan Fasilitas Hotel'),
            ('diskotik', 'Diskotik dan Klab Malam'),
            ('nsp', 'Nada Tunggu Telepon'),
            ('bank', 'Bank dan Kantor'),
            ('bioskop', 'Gedung Bioskop'),
            ('bazaar', 'Pameran dan Bazaar'),
            ('pesawat', 'Pesawat Terbang'),
            ('kereta', 'Transportasi Lain(Kereta, Bus, Kapal Laut)')
        ]
    )


class rekreasiForm(FlaskForm):
    # untuk Konser
    cekradio = RadioField(
        'Tiket?',
        choices=[
            ('Ya', 'Ya'),
            ('Tidak', 'Tidak')
        ]
    )
    htm = StringField(
        'Masukkan HTM',
        validators=[
            NumberRange(min=0)
        ]
    )
    pengunjung = StringField(
        'Masukkan Jumlah Pengunjung',
        validators=[
            NumberRange(min=0)
        ]
    )
    persen = StringField(
        'Persentase Penggunaan Musik',
        validators=[
            NumberRange(min=0, max=100, message='Masukkan presentase yang valid')
        ]
    )
    btnrekreasi = SubmitField('Hitung')


class nspForm(FlaskForm):
    # untuk nada sambung Telepon
    nsp = StringField(
        'Sambungan Telepon',
        validators=[
            NumberRange(min=0)
        ]
    )
    btnnsp = SubmitField('Hitung')


class hotelForm(FlaskForm):
    # untuk nada sambung Telepon
    hotelkamar = StringField(
        'Jumlah Kamar',
        validators=[
            NumberRange(min=0)
        ]
    )
    btnhotel = SubmitField('Hitung')


class diskoForm(FlaskForm):
    # untuk diskotik klub malam
    diskotikluas = StringField(
        'Luas Ruang (dalam Meter Persegi)',
        validators=[
            NumberRange(min=0)
        ]
    )
    btndiskotik = SubmitField('Hitung')


class pubForm(FlaskForm):
    # untuk pub, bar, bistro
    pubbarluas = StringField(
        'Luas Ruang (dalam Meter Persegi)',
        validators=[
            NumberRange(min=0)
        ]
    )
    btnpub = SubmitField('Hitung')


class restoForm(FlaskForm):
    # untuk resto dan kafe
    jmlkursi = StringField(
        'Jumlah Kursi',
        validators=[
            NumberRange(min=0)
        ]
    )
    btnresto = SubmitField('Hitung')


class mallForm(FlaskForm):
    # untuk Mall dkk
    luasruang = StringField(
        'Luas Ruang (dalam Meter Persegi)',
        validators=[
            NumberRange(min=0)
        ]
    )
    btnmall = SubmitField('Hitung')


class konserForm(FlaskForm):
    # untuk Konser
    konsercek = RadioField(
        'Tiket?',
        choices=[
            ('Ya', 'Ya'),
            ('Tidak', 'Tidak')
        ]
    )
    bproduksi = StringField(
        'Biaya Produksi',
        validators=[
            NumberRange(min=0)
        ]
    )
    grosstiket = StringField(
        'Penjualan Tiket (Gross)',
        validators=[
            NumberRange(min=0)
        ]
    )
    freetiket = StringField(
        'Tiket yang Digratiskan',
        validators=[
            NumberRange(min=0)
        ]
    )
    btnkonser = SubmitField('Hitung')


class karaokeForm(FlaskForm):
    # untuk nada sambung Telepon
    karaokeaula = StringField(
        'Karaoke Tanpa Kamar (Aula)',
        validators=[
            NumberRange(min=0)
        ]
    )
    karaokefamili = StringField(
        'Karaoke Family',
        validators=[
            NumberRange(min=0)
        ]
    )
    karaokeeksekutif = StringField(
        'Karaoke Eksekutif',
        validators=[
            NumberRange(min=0)
        ]
    )
    karaokebooth = StringField(
        'Karaoke Kubus (Booth)',
        validators=[
            NumberRange(min=0)
        ]
    )
    harikerja = StringField(
        'Hari Kerja',
        validators=[
            NumberRange(min=0)
        ]
    )
    btnkaraoke = SubmitField('Hitung')


class bankForm(FlaskForm):
    # untuk bank dan Kantor
    luasbankktr = StringField(
        'Luas Ruang (dalam Meter Persegi)',
        validators=[
            NumberRange(min=0)
        ]
    )
    btnbank = SubmitField('Hitung')


class bioskopForm(FlaskForm):
    # untuk bank dan Kantor
    jmllayar = StringField(
        'Jumlah Layar',
        validators=[
            NumberRange(min=0)
        ]
    )
    btnbioskop = SubmitField('Hitung')


class bazaarForm(FlaskForm):
    # untuk bazaar dan pameran
    hariAcara = StringField(
        'Jumlah Hari',
        validators=[
            NumberRange(min=0)
        ]
    )
    btnbazaar = SubmitField('Hitung')


class transportForm(FlaskForm):
    # untuk transportasi selain pesawat
    jmlpenumpang = StringField(
        'Jumlah Penumpang',
        validators=[
            NumberRange(min=0)
        ]
    )
    hrgtikettransport = StringField(
        'Harga Tiket Terendah',
        validators=[
            NumberRange(min=0)
        ]
    )
    durasimsk = StringField(
        'Durasi Musik Saat Perjalanan',
        validators=[
            NumberRange(min=0)
        ]
    )
    btntransport = SubmitField('Hitung')


class pesawatForm(FlaskForm):
    # untuk pesawat
    jmlpenumpangpswt = StringField(
        'Jumlah Penumpang',
        validators=[
            NumberRange(min=0)
        ]
    )
    hrgtiketpswt = StringField(
        'Harga Tiket Terendah',
        validators=[
            NumberRange(min=0)
        ]
    )
    durasimskpswt = StringField(
        'Durasi Musik Saat Perjalanan',
        validators=[
            NumberRange(min=0)
        ]
    )
    durasimskpswtog = StringField(
        'Durasi Musik On Ground',
        validators=[
            NumberRange(min=0)
        ]
    )
    btnpesawat = SubmitField('Hitung')
