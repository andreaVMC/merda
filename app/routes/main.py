from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.forms import ShitForm
from app.models import Shit, User, UserTeam, Team
from app import db

bp = Blueprint('main', __name__)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route('/home', methods=['GET'])
@login_required
def home():
    form = ShitForm()
    shits_users = (
        db.session.query(Shit, User)
        .join(User, Shit.userID == User.id)
        .all()
    )

    user_teams = (
        db.session.query(UserTeam.userID, Team)
        .join(Team, UserTeam.teamID == Team.id)
        .all()
    )

    user_teams_map = {}
    for user_id, team in user_teams:
        if user_id not in user_teams_map:
            user_teams_map[user_id] = []
        user_teams_map[user_id].append(team)

    shits = []
    for shit, user in shits_users:
        teams = user_teams_map.get(user.id, [])
        shits.append((shit, user, teams))
    shits.reverse()

    return render_template('logged/home.html', form=form, user=current_user, shits=shits)
