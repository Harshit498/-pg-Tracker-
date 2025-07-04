from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from models.models import db, User  # Import User model
import os
from werkzeug.security import generate_password_hash, check_password_hash

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = os.urandom(24)
    db.init_app(app)

    # Set up Flask-Login
    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Import models so they are registered
    with app.app_context():
        from models import models

    @app.route('/')
    def home():
        return render_template('home.html')

    @app.route('/listings')
    def listings():
        from models.models import PG
        query = PG.query
        location = request.args.get('location', '').strip()
        pg_type = request.args.get('type', '').strip()
        if location:
            query = query.filter(PG.city.ilike(f'%{location}%') | PG.address.ilike(f'%{location}%'))
        if pg_type:
            if pg_type in ['PG', 'Flat', 'Villa']:
                query = query.filter(PG.sharing_type.ilike(f'%{pg_type}%'))
        pgs = query.all()
        return render_template('listings.html', pgs=pgs)

    @app.route('/details/<int:pg_id>')
    def details(pg_id):
        from models.models import PG
        pg = PG.query.get_or_404(pg_id)
        return render_template('details.html', pg=pg)

    @app.route('/roommates')
    def roommates():
        from models.models import Roommate
        query = Roommate.query
        location = request.args.get('location', '').strip()
        budget = request.args.get('budget', '').strip()
        gender = request.args.get('gender', '').strip()
        if location:
            query = query.filter(Roommate.location.ilike(f'%{location}%'))
        if budget:
            try:
                budget_val = int(budget)
                query = query.filter(Roommate.budget <= budget_val)
            except ValueError:
                pass
        if gender:
            query = query.filter(Roommate.gender == gender)
        roommates = query.all()
        return render_template('roommates.html', roommates=roommates)

    @app.route('/tiffin')
    def tiffin():
        from models.models import TiffinService
        tiffins = TiffinService.query.all()
        return render_template('tiffin.html', tiffins=tiffins)

    @app.route('/events')
    def events():
        from models.models import Event
        events = Event.query.all()
        return render_template('events.html', events=events)

    @app.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            if User.query.filter((User.username == username) | (User.email == email)).first():
                flash('Username or email already exists.', 'danger')
                return render_template('signup.html')
            user = User(username=username, email=email)
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            flash('Account created! Please log in.', 'success')
            return redirect(url_for('login'))
        return render_template('signup.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                login_user(user)
                flash('Logged in successfully.', 'success')
                return redirect(url_for('home'))
            else:
                flash('Invalid username or password.', 'danger')
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        flash('You have been logged out.', 'info')
        return redirect(url_for('home'))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True) 