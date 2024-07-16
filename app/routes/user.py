# project/app/routes/user.py
from flask import Blueprint, render_template
from flask_login import login_required
from app.models import User

bp = Blueprint('user', __name__)

@bp.route("/settings")
@login_required
def settings():
    return render_template("logged/settings.html")

@bp.route("/user/", methods=['GET'])
@login_required
def users():
    users = User.query.all()

    return render_template("logged/all_users.html", users=users)

@bp.route("/user/<int:user_id>", methods=['GET'])
@login_required
def user(user_id):
    user_data = User.query.get(user_id)
    if not user_data:
        return 'Team not found 404'

    return str(user_data.__dict__)
