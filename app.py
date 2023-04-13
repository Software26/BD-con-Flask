import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#--- Aqui tenemos la ruta de donde esta el archivo el print es parque lo veamos por cosola
directorio = os.path.abspath(os.path.dirname(__file__))
print(directorio)
#----------------------------------------

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio,'datos.sqlite')
app.config['SQLALCHEMY_TRACK_MOODIFICACIONS'] = False

basededatos = SQLAlchemy(app)

#creaccion del modelo o base de datos

class Persona(basededatos.Model):
    __tablename__='Personas'
    
    id = basededatos.Column(basededatos.Integer,primary_key = True)
    nombre = basededatos.Column(basededatos.Texto)
    edad = basededatos.Column(basededatos.Integer)
    
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
       
    def __repr__(self):
        texto = "Persona : nombre ={} y edad={}".format()
        return super().__repr__() 
        
        super().__init__()