# from flask import Flask, render_template, request, redirect, url_for, session, flash
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'

# # Configure SQLite database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Initialize the database
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# # User model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(200), nullable=False)

# # Home route
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Registration (Sign Up) route for both GET and POST
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']

#         # Check if user exists
#         existing_user = User.query.filter_by(email=email).first()
#         if existing_user:
#             flash('Email already exists, try logging in.')
#             return redirect(url_for('login'))

#         # Hash the password and store the new user
#         hashed_password = generate_password_hash(password)
#         new_user = User(username=username, email=email, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()

#         flash('Registration successful, you can now log in!')
#         return redirect(url_for('login'))

#     return render_template('signup.html')

# # Login route for both GET and POST
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']

#         # Check if the user exists and verify the password
#         user = User.query.filter_by(email=email).first()
#         if user and check_password_hash(user.password, password):
#             session['user'] = user.username
#             flash(f"Welcome {user.username}!")
#             return redirect(url_for('dashboard'))
#         else:
#             flash('Invalid credentials, please try again.')
#             return redirect(url_for('login'))

#     return render_template('login.html')

# # Dashboard route (only accessible after login)
# @app.route('/dashboard')
# def dashboard():
#     if 'user' in session:
#         return render_template('dashboard.html', username=session['user'])
#     else:
#         flash('You need to log in first!')
#         return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dictionary to store user data
users = {}

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Registration (Sign Up) route for both GET and POST
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if user exists
        if email in users:
            flash('Email already exists, try logging in.')
            return redirect(url_for('login'))

        # Hash the password and store the new user in the dictionary
        hashed_password = generate_password_hash(password)
        users[email] = {'username': username, 'password': hashed_password}

        flash('Registration successful, you can now log in!')
        return redirect(url_for('login'))

    return render_template('signup.html')

# Login route for both GET and POST
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the user exists and verify the password
        user = users.get(email)
        if user and check_password_hash(user['password'], password):
            session['user'] = user['username']
            flash(f"Welcome {user['username']}!")
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials, please try again.')
            return redirect(url_for('login'))

    return render_template('login.html')

# Dashboard route (only accessible after login)
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', username=session['user'])
    else:
        flash('You need to log in first!')
        return redirect(url_for('login'))
# Chart page route
@app.route('/chart')
def chart():
    return render_template('chart.html')

# Train Guide (Dumbbell) page route
@app.route('/dumbbell')
def dumbbell():
    return render_template('dumbbell.html')

# Food Care (Utensils) page route
@app.route('/utensils')
def utensils():
    return render_template('utensils.html')

# Settings page route
@app.route('/settings')
def settings():
    return render_template('settings.html')
  


@app.route('/logout')
def logout():
    session.pop('user', None)  # Xóa thông tin người dùng khỏi session
    flash('You have been logged out.')  # Thông báo đăng xuất
    return redirect(url_for('index'))  # Chuyển hướng về trang index


if __name__ == '__main__':
    app.run(debug=True)
