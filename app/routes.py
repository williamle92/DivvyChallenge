from flask.json import jsonify
from app import app
from flask import render_template, request
from .models import Divvy


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'William'}
    return render_template('index.html', title="Home", user=user)


@app.route('/average', methods=['GET'])
def average():
    start = request.args.get('start')
    stop = request.args.get('stop')
    trips = Divvy.query.filter(Divvy.start_time > start).filter(Divvy.stop_time< stop).all()
    average_trip = 0
    for trip in trips:
        average_trip += trip.trip_duration
    average_trip /= len(trips)
    return jsonify({ "averageDuration": average_trip})




