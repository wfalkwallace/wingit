from flask import Flask, jsonify, render_template, request, session, redirect, flash

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
	return render_template("search.html")

@app.route("/search")
def search():
	return render_template("search.html")

@app.route("/results")
def results():
	return render_template("results.html")

if __name__ == "__main__":
	app.run(host="0.0.0.0")