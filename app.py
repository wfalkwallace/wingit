from flask import Flask, jsonify, render_template, request, session, redirect, flash

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
	return render_template("search.html")

@app.route("/search", methods=["POST"])
def search():
	if request.method == "POST":
		print 'signup-post'
		return render_template("signup.html", signup_email=request.form["register_email"])
	else: # request.method == "GET"
		return render_template("search.html")

@app.route("/results")
def results():
	return render_template("results.html")

@app.errorhandler(404)
def page_not_found(error):
	return render_template("results.html"), 404


if __name__ == "__main__":
	app.run(host="0.0.0.0")


