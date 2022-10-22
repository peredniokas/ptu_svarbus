from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    app.root_path, "movies.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Filmas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    director = db.Column(db.String(80))
    release_date = db.Column(db.DateTime)
    actors = db.Column(db.String(255))

    def release_year(self):
            return self.release_date.strftime("%Y")

    def actors_list(self):
            return self.actors.split(',')

class Director(db.Model):
    __tablename__ = "dirctors"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

class Actor(db.Model):
    __tablename__ = "actors"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

class Guildmembership(db.Model):
    __tablename__ = "member"
    id = db.Column(db.Integer,primary_key=True)
    guild = db.Column(db.String(255))


@app.route("/")
def hello():
    return "Sveiki Atvyke i crazy saly!!!"
    
if __name__ == "__main__":
    app.run()
