import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#--- Aqui tenemos la ruta de donde esta el archivo el print es parque lo veamos por cosola
directorio = os.path.abspath(os.path.dirname(__file__))
print(directorio)
#----------------------------------------

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio,'datos.sqlite')
app.config['SQLALCHEMY_tract'] 