"""
Models for SQL classes

"""

class Airport(db_name):
	__tablename__ = 'airports'

	airport_id = db_name.Column(db_name.Integer, primary_key = True))
	code = db_name.Column(db_name.String(3), unique = True)
	name = db_name.Column(db_name.String(64))
	city = name = db_name.Column(db_name.String(64))
	country = db_name.Column(db_name.String(64))
	created_at = db_name.Column(db_name.DateTime)

class Flight(db_name)
	__tablename__ = 'flights'
	flight_id = db_name.Column(db_name.Integer, primary_key = True)
	etd = db_name.Column(db_name.DateTime)
	eta = db_name.Column(db_name.DateTime)
	price = db_name.Column(db_name.Double)
	created_at = db_name.Column(db_name.DateTime)

	#foreign key
	origin = db.Column(db.Integer, db_name.ForeignKey('airports.airport_id'))
	dest = db.Column(db.Integer, db_name.ForeignKey('airports.airport_id'))

class Feature(db_name):
	__tablename__ = 'features'
	feature_id = db_name.Column(db_name.Integer, primary_key = True)
	temp = db_name.Column(db_name.Integer)
	beer_price = db_name.Column(db_name.Double)
	created_at = db_name.Column(db_name.DateTime)

	#foreign key
	place = db_name.Column(db_name.Integer, db_name.ForeignKey('airports.airport_id'))

