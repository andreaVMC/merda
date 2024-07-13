from flask import Blueprint, render_template
from flask_login import login_required, current_user
from app.models import Shit, User, Team
from app import db

bp = Blueprint('team', __name__)

@bp.route("/team/<int:team_id>", methods=['GET'])
@login_required
def team(team_id):

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

    return render_template("logged/team.html", team_info=team_info)