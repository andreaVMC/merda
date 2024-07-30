from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from app.models import UserTeam, Team
from app import db
from app.forms import TeamCreateForm, ShitForm

bp = Blueprint('team', __name__)

@bp.route("/team/", methods=['GET'])
@login_required
def teams():
    add_modal_form = ShitForm()
    teams = Team.query.all()

    return render_template("logged/all_teams.html", 
                           add_modal_form=add_modal_form, teams=teams)

@bp.route("/team/<int:team_id>", methods=['GET'])
@login_required
def team(team_id):
    add_modal_form = ShitForm()

    team_data = Team.query.get(team_id)
    if not team_data:
        return 'Team not found 404'

    team_info = {
        'id': team_data.id,
        'name': team_data.name,
        'users': []
    }

    for user_team in team_data.user_teams:
        user = user_team.user
        user_info = {
            'id': user.id,
            'nickname': user.nickname,
            'email': user.email,
            'name': user.name,
            'surname': user.surname,
            'sex': user.sex,
            'date_of_birth': user.date_of_birth,
            'weight': user.weight,
            "shits": []
        }
        
        for shit in user.shits:
            shit_info = {
                'id': shit.id,
                'shape': shit.shape,
                'quantity': shit.quantity,
                'color': shit.color.color,
                'dimension': shit.dimension,
                'level_of_satisfaction': shit.level_of_satisfaction,
                'notes': shit.notes,
                'created_at': shit.created_at
            }
            user_info['shits'].append(shit_info)

        team_info['users'].append(user_info)

    return render_template("logged/team.html", add_modal_form=add_modal_form, 
                           team_info=team_info)

@bp.route("/team/<int:team_id>/join", methods=['POST'])
@login_required
def team_join(team_id):
    team = Team.query.get_or_404(team_id)

    if UserTeam.query.filter_by(userID=current_user.id, teamID=team.id).first():
        return "You are already a member of this team"

    user_team = UserTeam(userID=current_user.id, teamID=team.id)
    db.session.add(user_team)
    db.session.commit()

    return f"You have successfully joined the team '{team.name}'"

@bp.route("/team/<int:team_id>/leave", methods=['POST'])
@login_required
def team_leave(team_id):
    team = Team.query.get_or_404(team_id)

    user_team = UserTeam.query.filter_by(userID=current_user.id, teamID=team.id).first()
    if not user_team:
        return "You are not a member of this team"

    db.session.delete(user_team)
    db.session.commit()

    return f"You have successfully left the team '{team.name}'"

@bp.route("/team/create", methods=['GET', 'POST'])
@login_required
def team_create():
    add_modal_form = ShitForm()
    form = TeamCreateForm()

    if form.validate_on_submit():
        existing_team = Team.query.filter_by(name=form.name.data).first()
        if existing_team:
            flash("A team with this name already exists", 'danger')
        else:
            new_team = Team(name=form.name.data)
            db.session.add(new_team)
            db.session.commit()

            flash(f"Team '{form.name.data}' has been created successfully", 'success')
            return "TOP FRA E' ANDATO TUTTO OK"

    return render_template('logged/team_create.html', 
                           add_modal_form=add_modal_form, form=form)
