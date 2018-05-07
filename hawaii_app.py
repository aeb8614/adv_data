import pandas as pd
import numpy as np
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#database
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)

#flask
hawaii_app = Flask(__name__)

@app.route("/")
def welcome():
    return (
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    percip_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date > year).all()
    precip = {date: prcp for date, prcp in precip_data}
    return jsonify(precip)

@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(Station.station).all()
    stations = list(np.ravel(stations))
    return jsonify(stations)


@app.route("/api/v1.0/tobs")
def temp_monthly():
    year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    temp_data = session.query(Measurement.tobs).filter(Measurement.date > year).all()
    temps = list(np.ravel(stations))

    # Return the results
    return jsonify(temps)

if __name__ == '__main__':
    app.run()

