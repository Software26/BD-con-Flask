import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy #Library is for connect to Database

directory = os.path.abspath(os.path.dirname(__file__))
print(directory)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(directory,'data.sqlite') # configure for file where is the direction of the app in database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database = SQLAlchemy(app)

# database model creation

class Person(database.Model): 
    __tablename__ = 'Person' # Name table Person
    
    # four fields for table
    id = database.Column(database.Integer, primary_key =  True) # 
    name = database.column(database.Text)
    age1 = database.Column(database.Integer)
    color = database.Column(database.Text)
   #---------------------------------------- 
    def __init__(self,name,age,color):
        self.name = name
        self.age = age  
        self.color  = color
        
    def __repr__(self):
        text = "Person : name = {}, age ={} and color = {}".format(self.name,self.age,self.color)
        return 