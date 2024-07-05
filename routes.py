from flask import render_template, redirect
from forms import RegisterForm, LoginForm
from flask_login import login_user, logout_user, current_user, login_required
from models import User
from ext import app, db

products = [
    {"name": "Apple airpods max", "price": "700", "image": "/static/apple headphones.jpg", "id": 0},
    {"name": "Samsung Galaxy S22", "price": "1200", "image": "/static/galaxys22.jpg", "id": 1},
    {"name": "House Of Marley: positive vibration 2", "price": "70", "image": "/static/headphones.jpg", "id": 2},
    {"name": "Iphone 13", "price": "1600", "image": "/static/iPhone13.png", "id": 3},


]


@app.route("/")
def index():
    return render_template("index.html", products=products)


@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():

    if current_user.is_authenticated:
        return redirect("/")


    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)


    return render_template("login.html", form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(password=form.password.data, username=form.username.data)

        db.session.add(new_user)
        db.session.commit()

        print(form.errors)


    return render_template("register.html", form=form)

@app.route("/registered_users")
@login_required
def users():

    if current_user.role != "admin":
        return redirect("/")

    registered_users = User.query.all()
    return render_template("users.html", registered_users=registered_users)

@app.route("/delete_user/<int:user_id>")
def delete_user(user_id):
    user = User.query.get(user_id)

    db.session.delete(user)
    db.session.commit()

    return redirect("/registered_users")

@app.route("/product/<int:product_id>")
def product(product_id):
    return render_template("product.html", product=products[product_id])
