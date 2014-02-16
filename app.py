from flask import Flask, jsonify, render_template, request, session, redirect, flash
from flask.ext.sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.debug = True
app.config.from_object('config.flask_config')
db = SQLAlchemy(app)
#from models import Flight, Airport, Feature

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

		# print request.form['oneway']
		# print request.form['roundtrip']
	
		all_flights = Flight.query.filter_by(
			origin = Airport.query.filter_by(code = origin).first().airport_id
			).all()

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
								price=price,
								trip_type=trip_type)
	else: # request.method == "GET"
		return render_template("search.html")

@app.route("/results")
def results():
	return render_template("results.html", flights = flights_dict)

@app.errorhandler(404)
def page_not_found(error):
	return render_template("404.html"), 404

#MODELS CODE ------------------------------------------------------
class Airport(db.Model):
	__tablename__ = 'airports'

	airport_id = db.Column(db.Integer, primary_key = True)
	code = db.Column(db.String(3), unique = True)
	#name = db.Column(db.String(64))
	city = db.Column(db.String(64))
	country = db.Column(db.String(64))
	created_at = db.Column(db.DateTime)

	def __init__(self, code, city, country):
		#self.airport_id = air_id
		self.code = code
		#self.name = name
		self.city = city
		self.country = country
		self.created_at = datetime.datetime.now()

class Flight(db.Model):
	__tablename__ = 'flights'
	
	flight_id = db.Column(db.Integer, primary_key = True)
	etd = db.Column(db.DateTime)
	eta = db.Column(db.DateTime)
	price = db.Column(db.Float)
	created_at = db.Column(db.DateTime)

	#foreign key
	origin = db.Column(db.Integer, db.ForeignKey('airports.airport_id'))
	dest = db.Column(db.Integer, db.ForeignKey('airports.airport_id'))

	def __init__(self, codez, etd, eta, price):
		#self.flight_id = air_id

		self.origin = Airport.query.filter_by(code = codez).first().airport_id
		self.dest = Airport.query.filter_by(code = codez).first().airport_id
		self.etd = etd
		self.eta = eta
		self.price = price
		self.create_at = datetime.datetime.now()


class Feature(db.Model):
	__tablename__ = 'features'
	feature_id = db.Column(db.Integer, primary_key = True)
	temp = db.Column(db.Integer)
	beer_price = db.Column(db.Float)
	created_at = db.Column(db.DateTime)

	#foreign key
	place = db.Column(db.Integer, db.ForeignKey('airports.airport_id'))

	def __init__(self, temp, beer_price, created_at):
		#self.feature_id = feature_id
		self.temp = temp
		self.beer_price = beer_price
		self.created_at = created_at 



if __name__ == "__main__":
	app.run(host="0.0.0.0")


