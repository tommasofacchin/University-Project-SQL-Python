from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_user, current_user


auth = Blueprint('auth', __name__,  template_folder='templates',
                 static_folder='static')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile.profile_page'))

    if request.method == 'POST':
        # Imports
        from db_helper import get_user
        from main import bcrypt
        from models import User

        email = request.form.get('email')
        password = request.form.get('password')
        user = get_user(User.email == email)

        if user:
            # Checking password
            res = bcrypt.check_password_hash(user.pwhash, password)
            if res:
                login_user(user)
                return redirect(url_for('profile.profile_page'))
            else:
                return render_template('login.html', error="Wrong password")
        else:
            return render_template('login.html', error="User not found")

    # GET request
    return render_template('login.html')


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('profile.profile_page'))

    if request.method == 'POST':
        # Imports
        from models import User
        from main import bcrypt
        from db_helper import add, get_user

        user = User(
                firstname=request.form.get('first-name'),
                lastname=request.form.get('last-name'),
                birthdate=request.form.get('dob').replace('-', ''),
                email=request.form.get('email'),
                pwhash=bcrypt.generate_password_hash(request.form.get('password'), 12),
            )

        # Role
        if request.form.get('role') == 'seller':
            user.seller = True

        check_pw = bcrypt.check_password_hash(
                user.pwhash,
                request.form.get('confirm-password')
            )

        if not check_pw:
            return render_template('register.html', error="Confirm password don't match")

        if get_user(User.email == user.email):
            return render_template('register.html', error="This email already exists")

        add(user)
        login_user(get_user(User.email == user.email))
        return redirect(url_for('profile.profile_page'))

    # GET request
    return render_template('register.html')
