from flask import Flask, jsonify, render_template, request, session, redirect, flash
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.debug = True
app.config.from_object('config.flask_config')
db = SQLAlchemy(app)
#from models import Flight, Airport, Feature

#MODELS CODE ------------------------------------------------------
# class Airport(db.Model):
# 	__tablename__ = 'airports'

# 	airport_id = db.Column(db.Integer, primary_key = True)
# 	code = db.Column(db.String(3), unique = True)
# 	#name = db.Column(db.String(64))
# 	city = db.Column(db.String(64))
# 	country = db.Column(db.String(64))
# 	created_at = db.Column(db.DateTime)

# 	def __init__(self, code, city, country):
# 		#self.airport_id = air_id
# 		self.code = code
# 		#self.name = name
# 		self.city = city
# 		self.country = country
# 		self.created_at = datetime.datetime.now()

# 	def __repr__(self):
# 		return "<Airport id = '%s', code = '%s', city = '%s', country = '%s'  >" % \
# 		(
# 			self.airport_id,
# 			self.code,
# 			self.city,
# 			self.country
# 		)

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
	city = db.Column(db.String(64))
	country = db.Column(db.String(64))
	temp = db.Column(db.Integer)
	beer_price = db.Column(db.Float)
	created_at = datetime.datetime.now()

	def __init__(self, city, country, temperature, beer_price):
		#self.feature_id = feature_id
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
		origin = request.form['from']
		depart_date = request.form['depart']
		return_date = request.form['return']
		price = request.form['price']

		print 'origin: ', origin 

		#origin_airport_id = Airport.query.filter_by(code = origin).first().airport_id

		#print 'origin_airport_id ', origin_airport_id

		all_airports = Airport.query.all()
		for airport in all_airports:
			print airport

		all_airports = Airport.query.count()
		print 'all_airport_count', all_airports
		all_flights = Flight.query.filter_by(
			origin = origin_airport_id
			).all()
		print 'all_flights', all_flights

		trip_type = request.form['trip-type']

		flight= []
		for item in all_flights:
			if item.price < price:
				if datetime.combine(depart_date.date, datetime.time.min) < item.etd and \
					item.etd < datetime.combine(depart_date.date, datetime.time.max):
						flights.append(item)
		


		#build db + query pint
		return render_template("results.html", 
								origin=origin, 
								depart_date=depart_date,
								return_date=return_date,
								price=price)
	else: # request.method == "GET"
		return render_template("search.html")

@app.route("/results")
def results():
	return render_template("results.html", flights = flights_dict)

@app.errorhandler(404)
def page_not_found(error):
	return render_template("404.html"), 404




if __name__ == "__main__":
	app.run(host="0.0.0.0")


