from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/shit_app'
app.config['SECRET_KEY'] = 'a'
DB.init_app(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    return render_template("logged/home.html")

@app.route("/settings")
def settings():
    return render_template("logged/settings.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)
