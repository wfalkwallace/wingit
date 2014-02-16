import MySQLdb
import datetime
import sys

#call: python populate.py <path_to_txt> <model>
#path to airport codes: '../flight_codes.txt'
#path to flight info: 

text_name= sys.argv[0]
model_type = sys.argv[1]

# Open database connection
db = MySQLdb.connect("wingit.crlh5pdu9hyk.us-east-1.rds.amazonaws.com",\
	"root","wingitrealgood","wingitdb")

# prepare a cursor object using cursor() method
cursor = db.cursor()
txt_file = open(, 'r')

    # flight_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    # origin INT NOT NULL,
    # dest INT NOT NULL,
    # etd DATETIME NOT NULL,
    # eta DATETIME NOT NULL,
    # price DECIMAL NOT NULL,
    # created_at DATETIME,

for line in txt_file:
	line_arr = line.rstrip().split(';')
	print 'line_arr', line_arr

	# Prepare SQL query to INSERT a record into the database.
	#parse text file

	if model_type == 'airport':
		sql = "INSERT INTO airports(code, city, country, created_at) VALUES ('%s', '%s', '%s', '%s')" % \
			( line_arr[2], line_arr[0], line_arr[1], str(datetime.datetime.now()) )
	if model_type == 'flight':
		sql = "INSERT INTO flight(origin, dest, etd, eta, price, created_at) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % \
			( line_arr[0], line_arr[1], line_arr[2], line_arr[3], line_arr[4], str(datetime.datetime.now()) )
	cursor.execute(sql)

try:
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
