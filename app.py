from datetime import datetime
from flask import Flask, render_template, url_for, flash, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, DecimalField, SelectField, IntegerField, TextAreaField
from wtforms.validators import InputRequired, Length, Email, ValidationError, Optional, NumberRange

from flask_bcrypt import Bcrypt

db = SQLAlchemy()
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@localhost:5432/shit_app'
app.config['SECRET_KEY'] = 'a'
db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    def __init__(self, nickname, email, password, name, surname, sex=None, 
                 date_of_birth=None, weight=None):
        self.nickname = nickname
        self.email = email
        self.password = password
        self.name = name
        self.surname = surname
        self.sex = sex
        self.date_of_birth = date_of_birth
        self.weight = weight
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nickname = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    sex = db.Column(db.String(1), nullable=True, 
                    check_constraint='sex IN (\'M\', \'F\')')
    date_of_birth = db.Column(db.Date, nullable=True)
    weight = db.Column(db.Numeric(5, 2), nullable=True, 
                       check_constraint='weight >= 0')
    

class Shit(db.Model):
    __tablename__ = 'shit'
    
    id = db.Column(db.Integer, primary_key=True)
    shape = db.Column(db.Integer, nullable=False, check_constraint='shape >= 1 AND shape <= 7')
    quantity = db.Column(db.Integer, nullable=False, check_constraint='quantity >= 0 AND quantity <= 10')
    colorID = db.Column(db.Integer, db.ForeignKey('shit_color.id'), nullable=False)
    dimension = db.Column(db.Integer, nullable=False, check_constraint='dimension >= 0 AND dimension <= 10')
    level_of_satisfaction = db.Column(db.Integer, nullable=False, check_constraint='level_of_satisfaction >= 0 AND level_of_satisfaction <= 10')
    userID = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)

    # Define relationships if necessary
    user = db.relationship('User', backref='shits')
    color = db.relationship('ShitColor', backref='shits')

    
    __table_args__ = (
        db.CheckConstraint('quantity >= 0 AND quantity <= 10', name='quantity_check'),
        db.CheckConstraint('dimension >= 0 AND dimension <= 10', name='dimension_check'),
        db.CheckConstraint('level_of_satisfaction >= 0 AND level_of_satisfaction <= 10', name='level_of_satisfaction_check'),
    )

    user = db.relationship('User', backref=db.backref('shits', cascade='all, delete-orphan'))


class ShitColor(db.Model):
    __tablename__ = 'shit_color'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)


class RegisterForm(FlaskForm):
    nickname = StringField(validators=[
        InputRequired(), Length(max=255)],
        render_kw={"placeholder": "Nickname"})
    
    email = StringField(validators=[
        InputRequired(), Email(), Length(max=255)], 
        render_kw={"placeholder": "Email"})
    
    password = PasswordField(validators=[
        InputRequired(), Length(min=8, max=20)], 
        render_kw={"placeholder": "Password"})
    
    name = StringField(validators=[
        InputRequired(), Length(max=50)], render_kw={"placeholder": "Name"})
    
    surname = StringField(validators=[
        InputRequired(), Length(max=50)], render_kw={"placeholder": "Surname"})
    
    sex = SelectField(choices=[('M', 'Male'), ('F', 'Female')],
                      validators=[Optional()], 
                      render_kw={"placeholder": "Sex"})
    
    date_of_birth = DateField(validators=[Optional()], format='%Y-%m-%d', 
                              render_kw={"placeholder": "Date of Birth"})
    
    weight = DecimalField(validators=[Optional()], places=2, rounding=None, 
                          render_kw={"placeholder": "Weight"})
    
    submit = SubmitField('Register')
    
    def validate_email(self, email):
        existing_user_email = User.query.filter_by(email=email.data).first()
        if existing_user_email:
            raise ValidationError('That email already exists. Please log in.')



class LoginForm(FlaskForm):
    email = StringField(validators=[
                           InputRequired(), Length(min=4, max=40)],
                            render_kw={"placeholder": "email"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], 
                             render_kw={"placeholder": "Password"})

    submit = SubmitField('Login')


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
    quantity = IntegerField('Quantity', validators=[InputRequired(), NumberRange(min=0, max=10)])
    colorID = SelectField('Color', choices=[
        ('1', 'Black'),
        ('2', 'Brown'),
        ('3', 'Green'),
        ('4', 'Yellow'),
        ('5', 'Red'),
        ('6', 'White'),
    ], validators=[InputRequired()])
    dimension = IntegerField('Dimension (1-10)', validators=[InputRequired(), NumberRange(min=1, max=10)])
    level_of_satisfaction = IntegerField('Level of Satisfaction (1-10)', validators=[InputRequired(), NumberRange(min=1, max=10)])
    notes = TextAreaField('Notes')
    submit = SubmitField('Record Shit')

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    # Fetch all shit records along with the related user
    shits = db.session.query(Shit, User).join(User, Shit.userID == User.id).all()
    
    # shit recording management
    form = ShitForm()
    if form.validate_on_submit():
        # Create a new Shit record and save it to the database
        shit = Shit(
            shape=form.shape.data,
            quantity=form.quantity.data,
            colorID=form.colorID.data,
            dimension=form.dimension.data,
            level_of_satisfaction=form.level_of_satisfaction.data,
            userID=current_user.id,
            notes=form.notes.data
        )
        db.session.add(shit)
        db.session.commit()
        flash('Registration successful!', 'success')  # Flash success message
        return redirect(url_for('home'))
    return render_template('logged/home.html', user=current_user, form=form, shits=shits)

@app.route("/settings")
@login_required
def settings():
    return render_template("logged/settings.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home')) 
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=True) # Could add "Remember me" btn
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')
    
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            new_user = User(
                nickname=form.nickname.data,
                email=form.email.data,
                password=hashed_password,
                name=form.name.data,
                surname=form.surname.data,
                sex=form.sex.data,
                date_of_birth=form.date_of_birth.data,
                weight=form.weight.data
            )
            db.session.add(new_user)
            try:
                db.session.commit()
                flash('Your account has been created! \
                      You are now able to log in', 'success')
                return redirect(url_for('login'))
            except Exception as e:
                db.session.rollback()
                flash('Error creating user: ' + str(e), 'danger')
        else:
            flash('Form validation failed', 'danger')
            for field, errors in form.errors.items():
                for error in errors:
                    flash(f"Error in {getattr(form, field).label.text}: {error}", 
                          'danger')
            # Log the errors to the console for debugging
            print("Form validation errors:", form.errors)

    return render_template('register.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
