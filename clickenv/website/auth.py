from flask import Blueprint, render_template, request, flash, url_for
 
auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/login/forget-password', methods=['GET', 'POST'])
def recover1():
    return render_template("forget-password.html")

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Enter a valid email', category='error')
        elif len(firstName) < 2 :
            flash('First name must be greater than 1 character', category='error')
        elif len(lastName) < 2 :
            flash('Last name must be greater than 1 character', category='error')
        elif len(password1) < 7 :
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account created!', category='success')

    return render_template("signup.html")