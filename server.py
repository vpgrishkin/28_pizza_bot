from flask import request, Response, redirect
from flask_admin import Admin, expose
from flask_admin.contrib.sqla import ModelView
from werkzeug.exceptions import HTTPException

from model import Meal, MealChoice
from app import app, db, ADMIN_LOGIN, ADMIN_PASSWORD


class AuthException(HTTPException):

    def __init__(self, message):
        super().__init__(message, Response(
            "Please refresh the page and enter login, password'", 401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}))


class AdminModelView(ModelView):

    def check_auth(self, username, password):
        return username == ADMIN_LOGIN and password == ADMIN_PASSWORD

    def is_accessible(self):
        auth = request.authorization
        if not auth or not self.check_auth(auth.username, auth.password):
            raise AuthException('Not authenticated.')
        return True


admin = Admin(app, name='Pizzashop', template_mode='bootstrap3')
admin.add_view(AdminModelView(Meal, db.session))
admin.add_view(AdminModelView(MealChoice, db.session))


@app.route('/')
def index():
    return redirect('/admin/')


if __name__ == '__main__':
    app.run()