from app import basededatos,Persona

basededatos.create_all()
#agremos esta personas en la tabla
persona1 = Persona("Antonio",34)
persona2 = Persona("Juan",30)

basededatos.session.add_all([persona1,persona2])
basededatos.session.commit()

#agremos esta persona en la tabla
persona3 = Persona("Natanael",32)
basededatos.session.add(persona3)
basededatos.session.commit()

#consultas
personas = Persona.query.all() # consultar todos los elemento que estan en esa tabla
print("Consultar todas las personas")
print(personas)


filtro1 = Persona.query.filter_by(nombre="Antonio") #una consulta por valores por columna
print("Filtro por elemento")
print(filtro1.all())

seleccion1 = Persona.query.get(2)
print("Busqueda por id")
print(seleccion1)