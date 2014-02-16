from flask import Flask, jsonify, render_template, request, session, redirect, flash

app = Flask(__name__)
app.debug = True

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
		trip_type = request.form['trip-type']

		print origin
		print depart_date
		print price
		print trip_type

		# print request.form['oneway']
		# print request.form['roundtrip']

	#db get by above; put into vars in dict as price, dest, ....
	#
	#api.get by above put into 
	# for api call
	# price =  resp.price 
	# dict["price" = price]
	#model for flights_dict:
	#list: 
	#item: {origin: JFK, dest:LHR, price:500, beer:1.62, },
	#build flights_dict here
	##add weather info to flights_dict
	#add beer info to flights_dict




		return render_template("results.html")
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


