# project/app/__init__.py
from flask import Flask, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = 'auth.login'
    login_manager.unauthorized_handler(unauthorized)

    with app.app_context():
        from .models import User
        from .routes import auth, main, user, api, team

        app.register_blueprint(auth.bp)
        app.register_blueprint(main.bp)
        app.register_blueprint(user.bp)
        app.register_blueprint(api.bp)
        app.register_blueprint(team.bp)

        db.create_all()

    return app

def unauthorized():
    flash('Please log in to access this page.', 'danger')
    return redirect(url_for('auth.login'))

@login_manager.user_loader
def load_user(user_id):
    from .models import User
    return User.query.get(int(user_id))
