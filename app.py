from flask import Flask, jsonify, render_template, request, session, redirect, flash
from flask.ext.sqlalchemy import SQLAlchemy
import requests
import datetime
app = Flask(__name__)
app.debug = True
app.config.from_object('config.flask_config')
db = SQLAlchemy(app)

#beer xml parsing setup
# import urllib
# from xml.etree import ElementTree as ET

#from models import Flight, Airport, Feature

#MODELS CODE ------------------------------------------------------
class Flight(db.Model):
	__tablename__ = 'flights'
	
	flight_id = db.Column(db.Integer, primary_key = True)
	dep_city = db.Column(db.String(64))
	dep_country = db.Column(db.String(64))
	dep_lat = db.Column(db.Float)
	dep_long = db.Column(db.Float)
	arr_city = db.Column(db.String(64))
	arr_country = db.Column(db.String(64))
	arr_lat = db.Column(db.Float)
	arr_long = db.Column(db.Float)
	depart = db.Column(db.DateTime)
	arrive = db.Column(db.DateTime)
	price = db.Column(db.Float)
	created_at = db.Column(db.DateTime)

	def __init__(self, departing_city, departing_country, departing_latitude, departing_longitude,
		arrival_city, arrival_country, arrival_latitude, arrival_longitude, depart, arrive, price):
		#self.flight_id = air_id
		self.dep_city = departing_city
		self.dep_country = departing_country
		self.dep_lat = departing_latitude
		self.dep_long = departing_longitude
		self.arr_city = arrival_city
		self.arr_country = arrival_city
		self.arr_lat = arrival_latitude
		self.arr_long = arrival_longitude
		self.depart = depart
		self.arrive = arrive
		self.price = price
		self.created_at = datetime.datetime.now()

class Feature(db.Model):
	__tablename__ = 'features'
	feature_id = db.Column(db.Integer, primary_key = True)
	city = db.Column(db.String(64))
	country = db.Column(db.String(64))
	temp = db.Column(db.Integer)
	beer_price = db.Column(db.Float)
	created_at = datetime.datetime.now()

	def __init__(self, city, country, temperature, beer_price):
		self.city = city
		self.country = country
		self.temp = temperature
		self.beer_price = beer_price
		self.created_at = datetime.datetime.now()


@app.route("/")
def home():
	return render_template("search.html")

@app.route("/search", methods=["GET", "POST"])
def search():
	if request.method == "POST":
		origin_city = request.form['from']
		# depart_date = request.form['depart']
		# return_date = request.form['return']
		price = request.form['price']

		# print 'origin: ', origin 

		# get from origin
		valid_flights_from_origin = Flight.query.filter_by(dep_city = origin_city,
															dep_country = "USA").all()
		# valid_flights_from_origin = Flight.query.all()
		print 'valid flights from origin', valid_flights_from_origin

		#flights with departure date, price, origin constricted.
		flight= []
		for item in valid_flights_from_origin:
			if int(item.price) < int(price):
				flight.append(item)

		# #beer pricing addition
		# requestURL = 'http://www.pintprice.com/xml.php?country=' + item.country.lower().replace(' ', '_')
		# root = ET.parse(urllib.urlopen(requestURL)).getroot()
		# print root
		# items = root.findall('city')
		# print items
		#fill dictionary
		flight_dict = {}
		for item in flight:
			flight_dict[item.arr_city] = {
				"dep_country" : item.dep_city,
				# "departing_datetime" : item.depart,
				# "departing_datetime" : item.arrive,
				"price" : item.price
				#"beer_price" : "",
				#"temperature" : ""
			}
			print item.arr_city

		

		#build db + query pint
		return render_template("results.html", 
								origin=origin_city, 
								# depart_date=depart_date,
								# return_date=return_date,
								max_price=price,
								flight_dict=flight_dict)
	else: # request.method == "GET"
		return render_template("search.html")

@app.route("/results")
def results():
	return render_template("results.html", flights = flights_dict)

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/contact/mail")
def mail():
	https://api.sendgrid.com/api/mail.send.json

@app.errorhandler(404)
def page_not_found(error):
	return render_template("search.html"), 404




if __name__ == "__main__":
	app.run(host="0.0.0.0")


