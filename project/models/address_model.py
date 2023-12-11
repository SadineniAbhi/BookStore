from project.extensions import db 
import datetime
from project.models.user_model import User
class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    flat_no = db.Column(db.Integer,nullable = False)
    house_no = db.Column(db.Integer,nullable = False)
    street_name = db.Column(db.String(100), nullable = False)
    city_name = db.Column(db.String(100),nullable = False)
    country_id = db.Column(db.ForeignKey('country.id'),nullable = False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))
    state_id = db.Column(db.Integer,db.ForeignKey('state.state_id'))
    created_date_time = db.Column(db.DateTime, default=datetime.datetime.now())
    last_updated = db.Column(db.DateTime, default=datetime.datetime.now())
    last_updated_by = db.Column(db.Integer,db.ForeignKey('user.id'))

#lookup tables
class Country(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    country_name = db.Column(db.String(100),nullable = False,unique = True)

class State(db.Model):
    state_id = db.Column(db.Integer, primary_key=True)
    Country_id = db.Column(db.Integer,db.ForeignKey('country.id'))
    state_name = db.Column(db.String(100),nullable = False,unique = True)

