import os
import argparse
import json
import sys

from app import db, app
from model import Meal, MealChoice, User



def load_file(filepath):
    if os.path.exists(filepath):
        return open(filepath, 'r', encoding='utf-8')


def load_data(json_file):
    return json.load(json_file)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-j', '--json_file', help='Input a json file path')
    parser.add_argument('-c', '--create', help='To create new db input: --create db')
    args = parser.parse_args()
    return args


def create_db():
    with app.app_context():
        db.drop_all()
        db.create_all()


def update_db_session(meals):
    for meal in meals:
        meals_to_db = Meal(title=meal["title"], description=meal["description"])
        for choice in meal["choices"]:
            meal_choice = MealChoice(title=choice["title"], price=choice["price"])
            meals_to_db.choices.append(meal_choice)
    
        db.session.add(meals_to_db)


if __name__ == '__main__':
    args = get_args()
    if args.create == 'db':
        print('Try to create the db')
        create_db()
    elif args.json_file:
        print('Try update db from {}'.format(args.json_file))
        json_file_path = args.json_file
        json_file = load_file(json_file_path)
        if json_file is None:
            print('No file: {}'.format(json_file_path))
            sys.exit(1)
        json_data = load_data(json_file)
        with app.app_context():
            update_db_session(json_data)
            db.session.commit()
    else:
        print('No arguments. Try -h')

