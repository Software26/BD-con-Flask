from app import basededatos,Persona

basededatos.create_all()
#we add this person in the table
persona1 = Persona("Antonio",34)
persona2 = Persona("Juan",30)

basededatos.session.add_all([persona1,persona2])
basededatos.session.commit()

#we add this person in the table
persona3 = Persona("Natanael",32)
basededatos.session.add(persona3)
basededatos.session.commit()

#-----consult---
#check all items
personas = Persona.query.all() 
print("Consultar todas las personas")
print(personas)

#a query column 
filtro1 = Persona.query.filter_by(nombre="Antonio") 
print("Filtro por elemento")
print(filtro1.all())  # all filter elements

seleccion1 = Persona.query.get(2)#search of id
print("Busqueda por id") 
print(seleccion1)

persona = Persona.query.get(1)
persona.edad = 45
basededatos.session.add(persona)
basededatos.session.commit()

persona_borrar = Persona.query.get(3)
basededatos.session.delete(persona_borrar)
basededatos.session.commit()
print("Se aborrado esta persona{}".format(persona_borrar))

personas = Persona.query.all()
print("Todos las Personas")
print(personas)

