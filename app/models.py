from sqlalchemy.orm import backref

from app import db

class Car(db.Model):
    __tablename__ = 'car'
    id = db.Column(db.Integer, primary_key=True)
    license_plate = db.Column(db.String(140))
    brand = db.Column(db.String(140))
    condition_id = db.Column(db.String(140))
    on_go = db.Column(db.Integer, db.ForeignKey('condition.id'))
    price = db.Column(db.String(64))
    link = db.Column(db.String(64))
    description = db.Column(db.String(640))
    prod_date = db.Column(db.DateTime)

    def __repr__(self):
        return "<Car {}>".format(self.brand)

class Condition(db.Model):
    __tablename__ = 'condition'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    car = db.relationship("Car", backref="condition", lazy='dynamic')
