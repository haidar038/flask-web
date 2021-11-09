from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('__name__', template_folder='sim/templates', static_folder='sim/static')
app.config['SECRET_KEY']="M Khaidar"
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///sim_pengaduan.db'
db = SQLAlchemy(app)

from sim.mahasiswa.routes import rmahasiswa
app.register_blueprint(rmahasiswa)