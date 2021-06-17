from app import db, migrate
from datetime import datetime

class Divvy(db.Model):
    trip_id = db.Column(db.Integer(), primary_key=True)
    start_time = db.Column(db.DateTime(), nullable=False)
    stop_time = db.Column(db.DateTime(), nullable=False)
    bike_id = db.Column(db.Integer(), nullable=False)
    from_station_id = db.Column(db.Integer(), nullable=False)
    from_station_name = db.Column(db.String(100), nullable=False)
    to_station_id = db.Column(db.Integer(), nullable=False)
    to_station_name = db.Column(db.String(100), nullable=False)
    user_type = db.Column(db.String(40), nullable=False)
    gender = db.Column(db.String(30))
    birthday = db.Column(db.String(50))
    trip_duration = db.Column(db.Integer(), nullable=False)

    def to_dict(self):
        return {
            'start': self.start_time,
            'stop' : self.stop_time
        }