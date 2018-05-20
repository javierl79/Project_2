from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, ForeignKey, Float, Text
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from flask_sqlalchemy import SQLAlchemy
from app import db

db = SQLAlchemy(app)

engine = create_engine("mysql+pymysql://root:tigers2@@6@localhost/baseball")

session = Session(engine)

metadata = MetaData()

Base = automap_base(metadata=metadata)

Base.prepare(engine, reflect=True)



# metadata.reflect(engine, )
class Value_Batting(db.Model):
    __tablename__= 'value_stats'
    name  = db.Column(db.String(60), index=True)
    Team = db.Column(db.String(60), index=True)
    Batting	= db.Column(db.Numeric(precision=9, scale=6))
    Base_Running = db.Column(db.Numeric(precision=9, scale=6))
    Fielding = db.Column(db.Numeric(precision=9, scale=6))
    Positional = db.Column(db.Numeric(precision=9, scale=6))
    Offense = db.Column(db.Numeric(precision=9, scale=6))
    Defense = db.Column(db.Numeric(precision=9, scale=6))
    League = db.Column(db.String(10), index=True)
    Replacement = db.Column(db.Numeric(precision=9, scale=6))
    RAR = db.Column(db.Numeric(precision=9, scale=6))
    WAR	= db.Column(db.Numeric(precision=9, scale=6))
    Dollars = db.Column(db.Numeric(precision=9, scale=6))
    playerid = db.Column(db.String(10), index=True, primary_key=True)


Player = Base.classes.name

print(Base.classes.players)

