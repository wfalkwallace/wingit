from flask import Flask
app = Flask(__name__)

#home page
@app.route("/")
def homepage():
	return "Welcome to the home page"

if __name__ == "__main__":
	app.run(host="0.0.0.0")
