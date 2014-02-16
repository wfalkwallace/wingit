import MySQLdb
import datetime

# Open database connection
db = MySQLdb.connect("wingit.crlh5pdu9hyk.us-east-1.rds.amazonaws.com","root","wingitrealgood","wingitdb")
# prepare a cursor object using cursor() method
cursor = db.cursor()

txt_file = open('../flight_codes.txt', 'r')

for line in txt_file:
	line_arr = line.rstrip().split(';')
	print 'line_arr', line_arr

	# Prepare SQL query to INSERT a record into the database.
	#parse text file

	a = line_arr[2]
	b = line_arr[0]
	c = line_arr[1]
	d = str(datetime.datetime.now())
	print a, ' , ', b,' , ', c,' , ', d
	sql = "INSERT INTO airports(code, city, country, created_at) VALUES ('%s', '%s', '%s', '%s')" % \
		( a, b, c, d )
	
	cursor.execute(sql)

try:
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
