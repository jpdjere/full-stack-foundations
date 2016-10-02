#Udacity: Full Stack Foundations


<h2>Build a data-driven web app with Python</h2>

<h2>LESSON 1</h2>

<h3>Working with the CRUD</h3>

Learn about CRUD; Create, Read, Update, and Delete.
Implement CRUD operations on a database.
Use an ORM (Object-Relational Mapping) as an alternative to SQL.


<h4>Problem Set 1</h4>

For this exercise you will be the database architect for the Uda County District of Animal Shelters. The shelters need a database for adopting dogs. his code should create a SQLite file called puppies.db in your working directory. <br >

<h2>LESSON 2</h2>

<h3>Making a Web Server</h3>

Build a web server from scratch using Python and some pre-installed libraries.
Learn how GET and POST requests can retrieve and modify information on a web site.
How to add CRUD functionality to our website.


<h2>LESSON 3</h2>

<h3>Developing with Frameworks</h3>

Introduction to web frameworks like Django and Ruby on Rails.
Use the Flask web framework to develop our own web application.
Introduction to APIs and how to add JSON endpoints to our application.

<h2>LESSON 4</h2>

<h3>Iterative Development</h3>

Build an entire web application on your own.
Learn about the iterative development process.
Have a working prototype throughout all stages of the development process.




------------------------------------------------------------------------------

Lesson 1 Review: CRUD

CRUD Review
Operations with SQLAlchemy
In this lesson, we performed all of our CRUD operations with SQLAlchemy on an SQLite database. Before we perform any operations, we must first import the necessary libraries, connect to our restaurantMenu.db, and create a session to interface with the database:

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
CREATE
We created a new Restaurant and called it Pizza Palace:
myFirstRestaurant = Restaurant(name = "Pizza Palace")
session.add(myFirstRestaurant)
sesssion.commit()
We created a cheese pizza menu item and added it to the Pizza Palace Menu:
cheesepizza = menuItem(name="Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course="Entree", price="$8.99", restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()
# READ We read out information in our database using the query method in SQLAlchemy:
firstResult = session.query(Restaurant).first()
firstResult.name

items = session.query(MenuItem).all()
for item in items:
    print item.name
UPDATE
In order to update and existing entry in our database, we must execute the following commands:

Find Entry
Reset value(s)
Add to session
Execute session.commit()
We found the veggie burger that belonged to the Urban Burger restaurant by executing the following query:
veggieBurgers = session.query(MenuItem).filter_by(name= 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"
Then we updated the price of the veggie burger to $2.99:

UrbanVeggieBurger = session.query(MenuItem).filter_by(id=8).one()
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit() 
DELETE
To delete an item from our database we must follow the following steps:

Find the entry
Session.delete(Entry)
Session.commit()
We deleted spinach Ice Cream from our Menu Items database with the following operations:

spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
session.delete(spinach)
session.commit() 
