from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.forms import ShitForm
from app.models import Shit, User
from app import db

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route('/home', methods=['GET'])
@login_required
def home():
    form = ShitForm()
    shits = db.session.query(Shit, User).join(User, Shit.userID == User.id).all()
    shits.reverse()
    return render_template('logged/home.html', form=form, user=current_user, shits=shits)
