# project/app/routes/user.py
from flask import Blueprint, render_template, redirect, flash, url_for
from flask_login import login_required, current_user
from app.models import User, Followers
from app import db

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

    return render_template("logged/user.html", user=user_data)

@bp.route("/user/<int:user_id>/follow", methods=['GET'])
@login_required
def user_follow(user_id):
    user_to_follow = User.query.get_or_404(user_id)
    
    if user_to_follow == current_user:
        flash('You cannot follow yourself!', 'warning')
        return redirect(url_for('main.home', user_id=user_id))
    
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
