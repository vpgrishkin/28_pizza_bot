from app import db


STANDART_STR_LENGTH = 256
SHORT_STR_LENGTH = 50


class Meal(db.Model):
    __tablename__ = "meals"
    id = db.Column(db.Integer, primary_key=True)
    choices = db.relationship('MealChoice', backref = 'meal', lazy='joined')
    title = db.Column(db.String(SHORT_STR_LENGTH))
    description = db.Column(db.String(STANDART_STR_LENGTH))

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __str__(self):
        return "{}: {}".format(self.title, self.description)


class MealChoice(db.Model):
    __tablename__ = 'meal_choices'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(SHORT_STR_LENGTH))
    price = db.Column(db.Integer)
    meal_id = db.Column(db.Integer, db.ForeignKey('meals.id'))

    def __init__(self, title=None, price=None):
        self.title = title
        self.price = price

    def __repr__(self):
        return '{} {} руб.'.format(self.title, self.price)
