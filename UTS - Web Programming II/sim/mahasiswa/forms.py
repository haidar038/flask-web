from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Length, Email

class mahasiswa_F(FlaskForm):
    npm = StringField('NPM', validators=[DataRequired(),Length(min=10, max=15)])
    nama = StringField('Nama', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    kelas = SelectField('Kelas',choices=[('-','-- Silakan Pilih Kelas'),('Info 1','Info 1'),('Info 2','Info 2'),('Info 3','Info 3'),('Info 4','Info 4'),('Info 5','Info 5')])
    alamat = TextAreaField('Alamat')
    submit = SubmitField('Tambah')
    password = PasswordField('Password', validators=[DataRequired(),Length(min=6, max=15)])
    conf_pass = PasswordField('Konfirmasi Password', validators=[DataRequired(),EqualTo('password')])

class login_M(FlaskForm):
    npm = StringField('NPM', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class uts_M(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    komentar = TextAreaField('Komentar', validators=[DataRequired()])
    submit = SubmitField('Kirim')