"""Form object declaration."""
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SubmitField,
    SelectField,
    RadioField
)
from wtforms.validators import (
    EqualTo,
    Length,
    URL
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
