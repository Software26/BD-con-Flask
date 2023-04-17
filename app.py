import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#--- Aqui tenemos la ruta de donde esta el archivo el print es parque lo veamos por cosola
directorio = os.path.abspath(os.path.dirname(__file__))
print(directorio)
#----------------------------------------

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directorio,'datos.sqlite')
app.config['SQLALCHEMY_TRACK_MOODIFICACIONS'] = False

basededatos = SQLAlchemy(app)

Migrate(app,basededatos)

#creaccion del modelo o base de datos

class Persona(basededatos.Model):
    __tablename__='Personas'
    
    id = basededatos.Column(basededatos.Integer,primary_key = True)
    nombre = basededatos.Column(basededatos.Text)
    edad = basededatos.Column(basededatos.Integer)
    color = basededatos.Column(basededatos.Text)
    
    def __init__(self,nombre,edad,color):
        self.nombre = nombre
        self.edad = edad
        self.color = color
       
    def __repr__(self):
        texto = "Persona : nombre ={} y edad={} color={}".format(self.nombre,self.edad,self.color)
        return texto
    
if __name__ == '__main__':
    app.run(debug=True)