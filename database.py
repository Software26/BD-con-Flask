from app1_connect import database, Person

database.create_all() #create table

# assignment two of values 
person1 = Person("Miguel",35)
person2 = Person("Antonio",28)

database.session.add_all([person1,person2]) #add all elements to table
database.session.commit()

# Assignment one of person
person3 = Person("Maria",30)
database.session.add(person3) # add value to database
database.session.commit()

# In the table person query all elements 
Persons = Person.query.all()
print("Consult all the People of table")
print(Persons)

# filter values by column
filter1 = Person.query.filter_by(name="Antonio")
print("Filter by name = Antonio")
print(filter1.all())

# Query by Filter of selection element
select1 = Person.query.get(2)
print("Search by id")
print(select1)

person4 = Person.query.get(1)
person4.age = 45 
database.session.add(person4)
database.session.commit()

# delete element of tablet
delete_person = Person.query.get(3)
database.session.delete(delete_person)
database.session.commit()
print("This person was deleted {}".format(delete_person))

Persons = Person.query.all()
print("Everybody")
print(Persons)


# add in query add
#Filter_by = Filter the specific element
# commit = updata the table
