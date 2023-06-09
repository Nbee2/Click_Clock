from flask import Blueprint, render_template, url_for, redirect

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@views.route('/blog', methods=['GET'])
def blog():
    return render_template("blog.html")

@views.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

@views.route('/portfolio', methods=['GET'])
def portfolio():
    return render_template("portfolio.html")

@views.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template("dashboard.html")