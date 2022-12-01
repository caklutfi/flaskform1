from flask_wtf import FlaskForm
from wtforms import (StringField, EmailField, IntegerField, TextAreaField, IntegerField, BooleanField, RadioField, SubmitField)
from wtforms.validators import InputRequired, Length

class ClientForm(FlaskForm):
    fullname = StringField('Name')
    email = EmailField('Email')
    phone = IntegerField('Nomor telepon/WA')
    address = StringField('Alamat')
    payment = StringField('Bukti transfer')
    dp = StringField('Besaran DP')
    session = StringField('Sesi')
    date = StringField('Tanggal')
    time = StringField('Waktu')
    instagram = StringField('Social media')
    reference = StringField('Dari mana anda mengetathui kami?')
    submit = SubmitField('Submit')