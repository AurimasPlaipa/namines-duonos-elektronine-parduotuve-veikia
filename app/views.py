

import os
import jwt
from flask import render_template, url_for, redirect, flash, request, abort
from flask_bootstrap import Bootstrap
from flask_login import current_user, login_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, logout_user, LoginManager, login_required, current_user
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps
from app import app, db, login_manager, bcrypt
from app.forms import LoginForm, RegisterForm, BreadForm
from app.models.User import User
from app.models.Bread import Bread
from app.models.Purchase import Purchase
from datetime import datetime, timezone, timedelta
from sqlalchemy.exc import IntegrityError

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 1:
            return abort(403)
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
def home():
    page = request.args.get('page', 1, type=int)
    all_breads = Bread.query.paginate(page=page, per_page=7, error_out=True)
    return render_template("index.html", all_breads=all_breads)

@app.route("/breads/<string:q>")
def selected_query(q):
    
    all_breads = Bread.query.filter_by(name=q)
    return render_template("selected-query.html", all_breads=all_breads)


@app.route("/my-bag")
def my_bag_page():
    # bagged_item to cart
    if current_user.is_anonymous:
        redirect(url_for("login"))

    in_cart = db.session.query(Purchase).filter(Purchase.purchaser_id == current_user.id, Purchase.paid is not True)
    in_cart = [pur.item_id for pur in in_cart]
    products_in_cart = [product for product in Bread.query.all() if product.id in in_cart]
    total_price = 0
    for product in products_in_cart:
        total_price += product.price
    return render_template("my-bag.html", purchases=products_in_cart, total=total_price)


@app.route("/to-bag")
def add_bread_to_bag():
    bread_id = request.args.get("bread_id")
    if not current_user.is_anonymous:
        existing_purchase = db.session.query(Purchase).filter(Purchase.bread_id == bread_id).first()
        print(existing_purchase)
        if not existing_purchase:
            # new purchase
            purchase = Purchase(paid=False, purchaser_id=current_user.get_id(), bread_id=bread_id)
            
            db.session.add(purchase)
            db.session.commit()
            flash("Ačiū kad pirkote.Laukiame sugrįžtant!")
            return redirect(url_for("home"))
        flash("Šis produktas jau krepšelyje", "error")
        return redirect(url_for("home"))
    flash("Prašome prisijungti, kad pradėtumėte apsipirkimą.", "error")
    return redirect(url_for('login'))


@app.route("/delete-from-bag")
def delete_from_bag():
    bread_id = request.args.get("bread_id")
    purchase = db.session.query(Purchase).filter(Purchase.bread_id == bread_id).first()
    if purchase:
        db.session.delete(purchase)
        db.session.commit()
    return redirect(url_for("my_bag_page"))


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Data from forms.
        user_email = form.email.data
        user_pass = form.password.data

       
        user = User.query.filter_by(email=user_email).first()
       
        if user:
            
            if check_password_hash(user.password, user_pass):
                login_user(user)
                return redirect(url_for("home"))
            else:
                flash("Neteisingas slaptažodis arba el. pašto adresas. Bandykite dar kartą.")
                return redirect(url_for("login"))
        else:
            flash("Nėra tokio el. pašto adreso")
            return redirect(url_for("login"))

    return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit() and form.validate():
        # hashed_and_salted_password = generate_password_hash(
        #     password=form.password.data,
        #     method="pbkdf2:sha256",
        #     salt_length=16)
        hashed_and_salted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        new_user = User(
            name=form.name.data,
            email=form.email.data,
            password=hashed_and_salted_password
        )
        db.session.add(new_user)
        db.session.commit()
        flash("Ačiū, kad užsiregistravote!")
        return redirect(url_for("login"))

    return render_template("register.html", form=form)


@app.route("/logout")
@login_required
def log_out():
    logout_user()
    return redirect(url_for("home"))


@app.route("/add-bread", methods=["GET", "POST"])
def add_bread():
    form = BreadForm()
    if form.validate_on_submit():
        filename = secure_filename(form.photo.data.filename)
        form.photo.data.save('static/uploads/' + filename)

        new_bread = Bread(
            name=form.name.data.title(),
            price=form.price.data,
            description =form.description.data,
            # photo_url='static/uploads/' + filename
        )
        # Add item to DB
        db.session.add(new_bread)
        db.session.commit()
        return redirect(url_for("add_bread"))

    return render_template("add-bread.html", form=form)


@app.route("/add-bread/<int:bread_id>")
def selected_bread(bread_id):

    requested_bread = Bread.query.get(bread_id)
    return render_template("selected-bread.html", requested_bread=requested_bread)


@app.route("/delete-bread/<int:bread_id>")
def delete_bread(bread_id):
    
    bread_to_delete = Bread.query.get(bread_id)
    db.session.delete(bread_to_delete)
    db.session.commit()
    flash("Prekė pašalinta iš krepšelio")
    return redirect(url_for("home"))

# def save_picture(form_picture):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(form_picture.filename)
#     picture_fn = random_hex + f_ext
#     picture_path = os.path.join(app.root_path, 'static/uploads', picture_fn)

#     output_size = (125, 125)
#     i = image.open(form_picture)
#     i.thumbnail(output_size)
#     i.save(picture_path)

#     return picture_fn    




