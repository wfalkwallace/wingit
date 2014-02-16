"""
Models for SQL classes

"""

import datetime

class Airport(db_name):
	__tablename__ = 'airports'

	airport_id = db_name.Column(db_name.Integer, primary_key = True))
	code = db_name.Column(db_name.String(3), unique = True)
	#name = db_name.Column(db_name.String(64))
	city = name = db_name.Column(db_name.String(64))
	country = db_name.Column(db_name.String(64))
	created_at = db_name.Column(db_name.DateTime)

	def __init__(self, code, city, country):
		#self.airport_id = air_id
		self.code = code
		#self.name = name
		self.city = city
		self.country = country
		self.created_at = datetime.datetime.now()

class Flight(db_name)
	__tablename__ = 'flights'
	flight_id = db_name.Column(db_name.Integer, primary_key = True)
	etd = db_name.Column(db_name.DateTime)
	eta = db_name.Column(db_name.DateTime)
	price = db_name.Column(db_name.Double)
	created_at = db_name.Column(db_name.DateTime)

	#foreign key
	origin = db_name.Column(db.Integer, db_name.ForeignKey('airports.airport_id'))
	dest = db_name.Column(db.Integer, db_name.ForeignKey('airports.airport_id'))

	def __init__(self, code, etd, eta, price):
		#self.flight_id = air_id

		self.origin = Airport(db_name).query.filter_by(code = code).first().airport_id
		self.dest = Airport(db_name).query.filter_by(code = code).first().airport_id
		self.etd = etd
		self.eta = eta
		self.price = price
		self.create_at = datetime.datetime.now()


class Feature(db_name):
	__tablename__ = 'features'
	feature_id = db_name.Column(db_name.Integer, primary_key = True)
	temp = db_name.Column(db_name.Integer)
	beer_price = db_name.Column(db_name.Double)
	created_at = db_name.Column(db_name.DateTime)

	#foreign key
	place = db_name.Column(db_name.Integer, db_name.ForeignKey('airports.airport_id'))

	def __init__(self, temp, beer_price, created_at):
		#self.feature_id = feature_id
		self.temp = temp
		self.beer_price = beer_price
		self.created_at = created_at 
