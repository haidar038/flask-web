from flask import Flask, render_template, redirect, url_for, Blueprint, flash
from sim.mahasiswa.forms import login_M, mahasiswa_F
from sim.models import Tmahasiswa, Tpengaduan
from sim import db

rmahasiswa = Blueprint("rmahasiswa",__name__)

@rmahasiswa.route("/")
def base():
    return render_template("base.html")

@rmahasiswa.route("/home")
def home():
    return render_template("home.html")

@rmahasiswa.route("/about")
def about():
    return render_template("about.html")

@rmahasiswa.route("/contact")
def contact():
    return render_template("contact.html")

@rmahasiswa.route("/data_mhsw", methods=['GET','POST'])
def data_m():
    form=mahasiswa_F()
    if form.validate_on_submit():
        add_mahasiswa = Tmahasiswa(npm=form.npm.data, nama=form.nama.data, email=form.email.data, password=form.password.data, kelas=form.kelas.data, alamat=form.alamat.data)
        db.session.add(add_mahasiswa)
        db.session.commit()
        flash(f'Akun {form.npm.data} Berhasil Daftar','success')
        return redirect(url_for('rmahasiswa.login_m'))
    return render_template("data_mhsw.html", form=form)

@rmahasiswa.route("/login_mhsw", methods=['GET','POST'])
def login_m():
    form=login_M()
    if form.validate_on_submit():
        return redirect(url_for('rmahasiswa.data_m'))
    return render_template("login_mhsw.html", form=form)



@rmahasiswa.route("/artikel/<info>")
def artikel(info):
    return "Halaman Artikel" + info ;