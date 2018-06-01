import datetime
import json
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

import pymysql
import decimal
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.sql import column as c
from sqlalchemy.sql import select
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, func, inspect, Table
from sqlalchemy.types import DECIMAL

# from models import Value_Batting

import os
import pandas as pd 
import numpy as np 
import plotly
import requests



#################################################
# Flask Setup
#################################################

app = Flask(__name__)
app.config["DEBUG"] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
#################################################
# Database Setup
#################################################
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:tigers2@@6@localhost/baseball'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:tigers2@@6@localhost/baseball'

app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

db.init_app(app)





class Batting(db.Model):
    __table_args__ = {"autoload": True, "autoload_with": db.engine}
    __tablename__ = "standardbatting"

class Batting_Advanced(db.Model):
    __table_args__ = {"autoload": True, "autoload_with": db.engine}
    __tablename__ = "advancedbatting"

class Batting_Value(db.Model):
    __table_args__ = {"autoload": True, "autoload_with": db.engine}
    __tablename__ = "valuebatting"

class Salary_Info(db.Model):
    __table_args__ = {"autoload": True, "autoload_with": db.engine}
    __tablename__ = "salaries"

class Player_Info(db.Model):
    __table_args__ = {"autoload": True, "autoload_with": db.engine}
    __tablename__ = "people"

class CPI_Info(db.Model):
    __table_args__ = {"autoload": True, "autoload_with": db.engine}
    __tablename__ = "cpi_info"

class Median_Income(db.Model):
    __table_args__ = {"autoload": True, "autoload_with": db.engine}
    __tablename__ = "real_median_hh_income"


#################################################
# Flask Routes
#################################################

def column_names(tableClass):
    names = map(lambda x: x.name, tableClass.__table__.columns)

    return list(names)

def get_data():
    cur = db.cursor(pymysql.cursors.DictCursor)
    cur.execute(sql)
    sql_results=cur.fetchall()

    cur.close()
    return sql_results

def object_as_dict(obj):
    return {c.key: getattr(obj, c.key)
        for c in inspect(obj).mapper.column_attrs}

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

# @app.route("/get-teams/$(team)", methods=['GET'])
@app.route("/get-teams")
def teams():
    team_data = []
    for row in db.session.query(Batting.Team).distinct():
        team_data.append(row)
    team_data = pd.DataFrame.from_dict(team_data)

    return team_data.to_json()



@app.route("/api/advanced-batting-data")
def advanced_data():
    advanced_data = []
    data = db.session.query(Batting_Advanced).all()
    for record in data:
        advanced_dict = {}
        for col in Batting_Advanced.__table__.columns:
            d = getattr(record, col.name)
            if isinstance(d, decimal.Decimal): d = float(d);
            advanced_dict[col.name] = d
        advanced_data.append(advanced_dict)
    return jsonify(advanced_data)

@app.route("/api/value-batting-data/<Player>")
def value_data(Player):
    value_data = []
    data = db.session.query(Batting_Value).all()
    for record in data:
        value_dict = {}
        for col in Batting_Value.__table__.columns:
            d = getattr(record, col.name)
            if isinstance(d, decimal.Decimal): d = float(d);
            value_dict[col.name] = d
        value_data.append(value_dict)

    return jsonify(value_data)

@app.route("/api/player-salaries")
def salary_data():
    salary_data = []
    data = db.session.query(Salary_Info).all()
    for record in data:
        salary_dict = {}
        for col in Salary_Info.__table__.columns:
            d = getattr(record, col.name)
            salary_dict[col.name] = d
        salary_data.append(salary_dict)

    return jsonify(salary_data)

@app.route("/api/player-bios")
def player_info():
    player_info = []
    data = db.session.query(Player_Info).all()
    for record in data:
        bio_dict = {}
        for col in Player_Info.__table__.columns:
            d = getattr(record, col.name)
            if isinstance(d, decimal.Decimal): d = float(d);
            bio_dict[col.name] = d
        player_info.append(bio_dict)

    return jsonify(player_info)

@app.route("/api/median-income")
def median_hh_income():
    median_hh_income = []
    data = db.session.query(Median_Income).all()
    for record in data:
        median_income_dict = {}
        for col in Median_Income.__table__.columns:
            d = getattr(record, col.name)
            if isinstance(d, decimal.Decimal): d = float(d);
            median_income_dict[col.name] = d
        median_hh_income.append(median_income_dict)

    return jsonify(median_hh_income)

@app.route("/api/cpi-data")
def cpi_data():
    cpi_data = []
    data = db.session.query(CPI_Info).all()
    for record in data:
        cpi_dict = {}
        for col in CPI_Info.__table__.columns:
            d = getattr(record, col.name)
            if isinstance(d, decimal.Decimal): d = float(d);
            cpi_dict[col.name] = d
        cpi_data.append(cpi_dict)

    return jsonify(cpi_data)



@app.route("/stats")
def stats():

    return render_template("stats.html")


@app.route("/")
def home():

	return render_template("index.html")


if __name__ == "__main__":
	app.run(debug=True)