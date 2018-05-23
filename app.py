import json
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, func, inspect, Table

# from models import Value_Batting

import os
import pandas as pd 
import numpy as np 
import plotly



#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Database Setup
#################################################
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tigers2@@6@localhost/baseball'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

# engine = create_engine('mysql+pymysql://root:tigers2@@6@localhost/baseball')
# metadata = MetaData(bind=engine)
# db.create_all()

class Batting(db.Model):
    __table_args__ = {"autoload": True, "autoload_with": db.engine}
    __tablename__ = "standardbatting"

class Batting_Advanced(db.Model):
    __table_args__ = {"autoload": True, "autoload_with": db.engine}
    __tablename__ = "advancedbatting"

# class Batting_Value(db.Model):
#     __table_args__ = {"autoload": True, "autoload_with": db.engine}
#     __tablename__ = "valuebatting"

# db.create_all()

#################################################
# Flask Routes
#################################################

@app.before_first_request
def setup():
	# db.drop_all()
	db.create_all()

@app.route("/api/standard-batting-data")
def batting_data():
    # standardbatting = Table('standardbatting', metadata, autoload=True)
    batting_data = []
    # data = standardbatting.query.all()
    data = db.session.query(Batting).all()
    for record in data:
        standard_dict = {}
        for col in Batting.__table__.columns:
            standard_dict[col.name] = getattr(record, col.name)
        batting_data.append(standard_dict)

    return jsonify(batting_data)

@app.route("/api/advanced-batting-data")
def advanced_data():
    advanced_data = []
    data = db.session.query(Batting_Advanced).all()
    for record in data:
        advanced_dict = {}
        for col in Batting_Advanced.__table__.columns:
            advanced_dict[col.name] = getattr(record, col.name)
        advanced_data.append(advanced_dict)

    return jsonify(advanced_data)

# @app.route("/api/value-batting-data/<value_batting>")
# def value_data():
#     value_data = []
#     data = db.session.query(Player).all()
#     for record in data:
#         value_dict = {}
#         value_data.append(value_dict)


    # value_data = []
    # data = db.session.query(Batting_Value).all()
    # for record in data:
    #     value_dict = {}
    #     for col in Batting_Value.__table__.columns:
    #         value_dict[col.name] = getattr(record, col.name)
    #     value_data.append(value_dict)

    # return jsonify(value_data)

@app.route("/")
def home():
    try:
        db.session.query('1').from_statement('SELECT 1').all()
        return '<h1>It works</h1>'
    except:
        return '<h1>Something is broken</h1>'
	# return render_template("index.html")

# @app.route("/stats")
# def stats():

if __name__ == "__main__":
	app.run(debug=True)