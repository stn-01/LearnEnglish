import os

from flask_admin import Admin
from flask import Flask, render_template
from flask_login import LoginManager
from webapp.admin_panel import DashboardView, UserView
from webapp.user.models import db, User

from webapp.user.views import blueprint as blueprint_user
from webapp.email.send_email import blueprint as blueprint_mail
from webapp.content.views import blueprint as blueprint_content
from webapp.translator.views import blueprint as blueprint_translator


def create_app():
    app = Flask(__name__, template_folder=os.path.join(os.getcwd(),
                'webapp/templates'))
    app.config.from_pyfile('config.py')
    app.app_context().push()
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'users.login'

    admin = Admin(app, index_view=DashboardView(),
                  endpoint='admin')
    admin.add_view(UserView(User, db.session, name='Пользователи'))

    app.register_blueprint(blueprint_user)
    app.register_blueprint(blueprint_mail)
    app.register_blueprint(blueprint_content)
    app.register_blueprint(blueprint_translator)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def homepage():
        return render_template('index.html', page_title='Главная')

    return app
