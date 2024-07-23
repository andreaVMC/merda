# project/app/routes/user.py
from flask import Blueprint, request, render_template, redirect, flash, url_for
from flask_login import login_required, current_user
from app.forms import ShitForm
from app.models import User, Followers, Team, UserTeam
from app import db

bp = Blueprint('user', __name__)

@bp.route("/settings")
@login_required
def settings():
    form = ShitForm()
    user_id = current_user.id
    user = User.query.get(user_id)

    teams = Team.query.all()
    all_users = User.query.all()

    user_teams = [user_team.teamID for user_team in user.user_teams]
    user_followers = [follower.follower for follower in Followers.query.filter_by(followee=user_id).all()]

    return render_template('logged/settings.html', form=form, user=current_user, teams=teams, all_users=all_users, user_teams=user_teams, user_followers=user_followers)

@bp.route('/update_user', methods=['POST'])
def update_user():
    # Retrieve user ID from the form
    user_id = request.form.get('id')
    user = User.query.get(user_id)

    if not user:
        return "User not found"

    # Update user attributes from form data
    user.nickname = request.form.get('nickname')
    user.email = request.form.get('email')
    user.password = request.form.get('password')  # Ensure to hash the password in a real-world scenario
    user.name = request.form.get('name')
    user.surname = request.form.get('surname')
    user.sex = request.form.get('sex')
    user.date_of_birth = request.form.get('date_of_birth')
    user.weight = request.form.get('weight')

    # Commit changes to the user details
    db.session.commit()

    # Update teams
    selected_team_ids = request.form.getlist('teams')
    UserTeam.query.filter_by(userID=user_id).delete()
    for team_id in selected_team_ids:
        user_team = UserTeam(userID=user_id, teamID=int(team_id))
        db.session.add(user_team)

    # Update followers
    selected_follower_ids = request.form.getlist('followers')
    Followers.query.filter_by(followee=user_id).delete()
    for follower_id in selected_follower_ids:
        follower = Followers(follower=int(follower_id), followee=user_id)
        db.session.add(follower)

    # Commit changes to teams and followers
    db.session.commit()

    return redirect(url_for('user.settings'))

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

    return render_template("logged/user.html", user=user_data)

@bp.route("/user/<int:user_id>/follow", methods=['GET'])
@login_required
def user_follow(user_id):
    user_to_follow = User.query.get_or_404(user_id)
    
    if user_to_follow == current_user:
        flash('You cannot follow yourself!', 'warning')
        return redirect(url_for('user.user', user_id=user_id))
    
    if not current_user.is_following(user_to_follow):
        follow = Followers(follower=current_user.id, followee=user_to_follow.id)
        db.session.add(follow)
        db.session.commit()
        flash(f'You are now following {user_to_follow.nickname}!', 'success')
    else:
        flash(f'You are already following {user_to_follow.nickname}.', 'info')
    
    return redirect(url_for('user.user', user_id=user_id))

@bp.route("/user/<int:user_id>/unfollow", methods=['GET'])
@login_required
def user_unfollow(user_id):
    user_to_unfollow = User.query.get_or_404(user_id)
    
    if user_to_unfollow == current_user:
        flash('You cannot unfollow yourself!', 'warning')
        return redirect(url_for('main.user_profile', user_id=user_id))
    
    if current_user.is_following(user_to_unfollow):
        Followers.query.filter_by(follower=current_user.id, followee=user_to_unfollow.id).delete()
        db.session.commit()
        flash(f'You have unfollowed {user_to_unfollow.nickname}.', 'success')
    else:
        flash(f'You are not following {user_to_unfollow.nickname}.', 'info')
    
    return redirect(url_for('user.user', user_id=user_id))
