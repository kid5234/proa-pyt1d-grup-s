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
            ('rekreasi', 'Pusat Rekreasi'),
            ('konser', 'Konser Musik'),
            ('karaoke', 'Karaoke (Rumah Bernyanyi)'),
            ('restokafe', 'Restauran dan Kafe'),
            ('pubbar', 'Pub, Bar, dan Bistro'),
            ('maldsb', 'Mall, Supermarket, Toko, Distro, Salon Kecantikan, Pusat Kebugaran, Arena Olahraga, Ruang Pamer'),
            ('hotel', 'Hotel'),
            ('diskotik', 'Diskotik'),
            ('nsp', 'Nada Tunggu Telepon'),
            ('bank', 'Bank dan Kantor'),
            ('bioskop', 'Gedung Bioskop'),
            ('bazaar', 'Pameran dan Bazaar'),
            ('pesawat', 'Pesawat Terbang'),
            ('kereta', 'Transportasi Lain(Kereta, Bus, Kapal Laut)')
        ]
    )


class nspForm(FlaskForm):
    # untuk nada sambung Telepon
    nsp = StringField(
        'Sambungan Telepon',
        validators=[
            NumberRange(min=0)
        ]
    )
    btnnsp = SubmitField('Hitung')


class bankForm(FlaskForm):
    # untuk bank dan Kantor
    luasbankktr = StringField(
        'Luas Area',
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
