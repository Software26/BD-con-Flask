from app import basededatos, Persona

persona =  Persona.query.get(1)
persona.color = "verde"
basededatos.session.add(persona)
basededatos.session.commit()

personas = Persona.query.all()
print(personas)

# fin out 
# python finout.py
