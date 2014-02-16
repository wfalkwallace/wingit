import MySQLdb
import datetime
import sys

# Open database connection
db = MySQLdb.connect("wingit.crlh5pdu9hyk.us-east-1.rds.amazonaws.com","root","wingitrealgood","wingitdb")
# prepare a cursor object using cursor() method
cursor = db.cursor()

txt_file = open('../flight_codes.txt', 'r')

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
	if 
	sql = "INSERT INTO airports(code, city, country, created_at) VALUES ('%s', '%s', '%s', '%s')" % \
		( line_arr[2], line_arr[0], line_arr[1], str(datetime.datetime.now()) )
	
	cursor.execute(sql)

try:
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
