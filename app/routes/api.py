from flask import Blueprint, redirect, url_for, flash
from flask_login import login_required, current_user
from app.forms import ShitForm
from app.models import Shit
from app import db
from datetime import datetime

bp = Blueprint('api', __name__)

@bp.route('/new_shit', methods=["POST"])
@login_required
def new_shit():
    form = ShitForm()
    
    if form.validate_on_submit():
        created_at = form.created_at.data if form.created_at.data else datetime.now()
        shit = Shit(
            shape=form.shape.data,
            quantity=form.quantity.data,
            colorID=form.colorID.data,
            dimension=form.dimension.data,
            level_of_satisfaction=form.level_of_satisfaction.data,
            userID=current_user.id,
            notes=form.notes.data,
            created_at=created_at
        )
        db.session.add(shit)
        db.session.commit()
        flash('Shit registration successful!', 'success')
        return redirect(url_for('main.home'))
    
    flash('Shit registration not successful!', 'error')
    return redirect(url_for('main.home'))
