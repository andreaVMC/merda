# project/app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, DecimalField, SelectField, IntegerField, TextAreaField, DateTimeLocalField
from wtforms.validators import InputRequired, Length, Email, ValidationError, Optional, NumberRange
from .models import User

class RegisterForm(FlaskForm):
    nickname = StringField(validators=[InputRequired(), Length(max=255)], render_kw={"placeholder": ""})
    email = StringField(validators=[InputRequired(), Email(), Length(max=255)], render_kw={"placeholder": ""})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": ""})
    name = StringField(validators=[InputRequired(), Length(max=50)], render_kw={"placeholder": ""})
    surname = StringField(validators=[InputRequired(), Length(max=50)], render_kw={"placeholder": ""})
    sex = SelectField(choices=[('M', 'Male'), ('F', 'Female')], validators=[Optional()])
    date_of_birth = DateField(validators=[Optional()], format='%Y-%m-%d', render_kw={"placeholder": ""})
    weight = DecimalField(validators=[Optional()], places=2, rounding=None, render_kw={"placeholder": ""})
    submit = SubmitField('Sign Up', render_kw={'class': 'btn filled submit-btn'})
    
    def validate_email(self, email):
        existing_user_email = User.query.filter_by(email=email.data).first()
        if existing_user_email:
            raise ValidationError('This email already exists. Please log in.')

class LoginForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Length(min=4, max=40)], render_kw={"placeholder": ""})
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": ""})
    submit = SubmitField('Login', render_kw={'class': 'btn filled submit-btn'})

class ShitForm(FlaskForm):
    shape = SelectField('Shape', choices=[
        ('1', 'Type 1: Separate hard lumps, like nuts (hard to pass)'),
        ('2', 'Type 2: Sausage-shaped, but lumpy'),
        ('3', 'Type 3: Like a sausage but with cracks on the surface'),
        ('4', 'Type 4: Like a sausage or snake, smooth and soft'),
        ('5', 'Type 5: Soft blobs with clear-cut edges (passed easily)'),
        ('6', 'Type 6: Fluffy pieces with ragged edges, a mushy stool'),
        ('7', 'Type 7: Watery, no solid pieces (entirely liquid)'),
    ], validators=[InputRequired()])
    quantity = IntegerField('Quantity', validators=[InputRequired(), NumberRange(min=0, max=10)], render_kw={"placeholder": ""})
    colorID = SelectField('Color', choices=[
        ('1', 'Black'),
        ('2', 'Brown'),
        ('3', 'Green'),
        ('4', 'Yellow'),
        ('5', 'Red'),
        ('6', 'White'),
    ], validators=[InputRequired()])
    dimension = IntegerField('Dimension (1-10)', validators=[InputRequired(), NumberRange(min=1, max=10)])
    level_of_satisfaction = IntegerField('Level of Satisfaction (1-10)', validators=[InputRequired(), NumberRange(min=1, max=10)], render_kw={"placeholder": ""})
    notes = TextAreaField('Notes')
    created_at = DateTimeLocalField('Created At', format='%Y-%m-%dT%H:%M', validators=[InputRequired()])
    submit = SubmitField('Record Shit')
