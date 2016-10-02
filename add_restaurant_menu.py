from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

#------------------------------------------CREATE------------------------------
session = DBSession()
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
session.commit()


cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with natural ingredients", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)
session.add(cheesepizza)


#------------------------------------------READ------------------------------
restaurants = session.query(Restaurant).all()
items = session.query(MenuItem).all()

for res in restaurants:
	for it in items:
		print(str(res.name)+" - "+str(it.name))




#------------------------------------------UPDATE------------------------------
veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggie in veggieBurgers:
	print(str(veggie.id) + " " + veggie.price + " " + veggie.restaurant.name + " " + "\n")

urbanVeggieBurger = session.query(MenuItem).filter_by(id = 9).one()
#print(urbanVeggieBurger.price +" "+urbanVeggieBurger.name+" "+ str(urbanVeggieBurger.id))


urbanVeggieBurger.price = "$2.99"
session.add(urbanVeggieBurger)
session.commit()

veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggie in veggieBurgers:
	print(str(veggie.id) + " " + veggie.price + " " + veggie.restaurant.name + " " + "\n")


#######----------Hago update de precio de todas las Veggie Burgers
for veggie in veggieBurgers:
	if veggie.price != '$2.99':
		veggie.price = '$2.99'
		session.add(veggie)
		session.commit()

veggieBurgers = session.query(MenuItem).filter_by(name = 'Veggie Burger')
for veggie in veggieBurgers:
	print(str(veggie.id) + " " + veggie.price + " " + veggie.restaurant.name + " " + "\n")






#------------------------------------------DELETE------------------------------
spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
print()
print(spinach.restaurant.name)

session.delete(spinach)
session.commit()

#spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()