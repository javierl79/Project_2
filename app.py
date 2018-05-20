import json
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
import pymongo

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

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/battingStatsComplete.sqlite'
db = SQLAlchemy(app)



# basedir = os.path.abspath(os.path.dirname(__file__))

# standardBatting = Base.classes.standard



#################################################
# Flask Routes
#################################################

def import_content(filepath):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['batter_stats_db'] #Replace mongo db name
    stats_collection = 'stats_collection' #Replace mongo db collection name
    db_cm = mng_db[stats_collection]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res)
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.remove()
    db_cm.insert(data_json)

if __name__ == "__main__":
  filepath = '/db/' + data  # pass csv file path
  import_content(filepath)

@app.before_first_request
def setup():
	db.drop_all()
	db.create_all()

@app.route("/api/batting-data")
def batting_data():
	df = pd.read_csv('db/standardBatting.csv')
	df.to_sql(name = 'standardBatting', con=db.engine, index=False)
	standard_stats = []
	for player in session.query(df.Name).all():
		standard_stats.append(player[0])

	return jsonify(standard_stats)


@app.route("/")
def home():
	return render_template("index.html")

# @app.route("/stats")
# def stats():

if __name__ == "__main__":
	app.run(debug=True)