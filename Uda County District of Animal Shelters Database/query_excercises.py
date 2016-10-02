from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Shelter, Puppy
from datetime import datetime, timedelta
from operator import itemgetter

engine = create_engine('sqlite:///shelter_puppy_db.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()


#Question 1 ------ Query all of the puppies and return the results in ascending alphabetical order

puppies = session.query(Puppy.name).all()
names = []
for i in puppies:
	names.append(i[0])

names.sort()
for i in names:
	print(i)



#Question 2 ----------- Query all of the puppies that are less than 6 months old organized by the youngest first
present = datetime.now()
allPuppies = session.query(Puppy.name, Puppy.dateOfBirth).all()
puppies6months = []
for i in allPuppies:
	birth = i[1]
	months = present - birth
	months = months.days / 30
	if months < 6:
		i = i + (months,)
		puppies6months.append(i)
print(puppies6months)
l2 = sorted(puppies6months, key=lambda x: float(x[2]))
print()
print(l2)


present = datetime.now()
limitDate = present - timedelta(days=180)
print(limitDate)
allPuppies = session.query(Puppy.name, Puppy.dateOfBirth).filter(Puppy.dateOfBirth > limitDate)
for i in allPuppies:
	print(str(i[0]) + " - " + str(i[1]))


#Question 3 -------------- Query all puppies by ascending weight

allPuppiesWeight = session.query(Puppy.name, Puppy.weight).order_by(Puppy.weight)
for i in allPuppiesWeight:
	print(str(i[0]) + " - " + str(i[1]))



#Question 4 --------------- Query all puppies grouped by the shelter in which they are staying
allPuppiesGrouped = session.query(Shelter.id, func.count(Puppy.id).label("amount")).join(Puppy).group_by(Shelter.id).all()

for i in allPuppiesGrouped:
	print(str(i.id) + " - " + str(i.amount))



result = session.query(Shelter, func.count(Puppy.id)).join(Puppy).group_by(Shelter.id).all()
for item in result:
	print(item[0].id, item[0].name, item[1])