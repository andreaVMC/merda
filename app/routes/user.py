# project/app/routes/user.py
from flask import Blueprint, render_template
from flask_login import login_required

bp = Blueprint('user', __name__)

@bp.route("/settings")
@login_required
def settings():
    return render_template("logged/settings.html")
