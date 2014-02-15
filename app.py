from flask import Flask, jsonify, render_template, request, session, redirect, flash

app = Flask(__name__)
app.debug = True

@app.route("/")
def home():
	return render_template("index.html")

if __name__ == "__main__":
	app.run(host="0.0.0.0")