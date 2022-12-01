from flask_wtf import FlaskForm
from wtforms import (StringField, EmailField, DateField, FileField, TimeField, TextAreaField, IntegerField, BooleanField, RadioField, SubmitField)
from wtforms.validators import InputRequired, Length

class ClientForm(FlaskForm):
    fullname = StringField('Name')
    email = EmailField('Email')
    phone = StringField('Nomor telepon/WA')
    address = StringField('Alamat')
    payment = FileField('Bukti transfer')
    dp = StringField('Besaran DP')
    session = StringField('Sesi')
    date = DateField('Tanggal')
    time = TimeField('Waktu')
    instagram = StringField('Social media')
    reference = StringField('Dari mana anda mengetathui kami?')
    submit = SubmitField('Submit')