import datetime as dt
import numpy as np
import pandas as pd

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################
#from flask_sqlalchemy import SQLAlchemy
# The database URI
#app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/battingStatsComplete.sqlite"

#db = SQLAlchemy(app)

#class Years(db.Model):
 #   __tablename__ = 'players_cleaned'

#    id = db.Column(db.Integer, primary_key=True)
 #   playerID = db.Column(db.String(64))
  #  salary = db.Column(db.Integer)
   # birthCountry = db.Column(db.String(64))
    #birthState = db.Column(db.String(64))
    #yearID = db.Column(db.Integer)
    #birthYear = db.Column(db.Integer)


 #   def __repr__(self):
 #       return '<Years %r>' % (self.playerID)

# Create database tables
#@app.before_first_request
#def setup():
    # Recreate database each time for demo
    #db.drop_all()
#    db.create_all()

#################################################
# Flask Routes
#################################################

@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")

#@app.route("/state_char")
#def state_char():
   # 

 
#    results = db.session.query(Years.birthState, Years.salary).\
 #       order_by(Years.salary.desc()).all()

    # Select the top 10 query results
#     birhtState = [result[0] for result in results]
#     salaries = [int(result[1]) for result in results]

#     # Generate the plot trace
#     plot_trace = {
#         "x": birhtState,
#         "y": salaries,
#         "type": "bar"
#     }
#     return jsonify(plot_trace)



# @app.route("/year_id")
# def year_char():
#    

#     #query for the emoji data using pandas
#     query_statement = db.session.query(Years).\
#     order_by(Years.yearID.asc()).statement
#     df = pd.read_sql_query(query_statement, db.session.bind)
    
#      #Format the data for Plotly
#     plot_trace = {
#             "x": df["yearID"].values.tolist(),
#             "y": df["salary"].values.tolist(),
#             "type": "bar"
#     }
#     return jsonify(plot_trace)


if __name__ == '__main__':
    app.run(debug=True)
