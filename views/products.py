from flask import Blueprint, render_template, request, redirect, url_for
from models.product import Product
from orm.setting import db

products_bp = Blueprint("products", __name__)


@products_bp.route("/")
def index():
    products = Product.query.order_by(Product.id.desc())
    return render_template("products/index.jinja", products=products)


@products_bp.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        price = request.form["price"]
        product = Product(title=title, description=description, price=price)

        db.session.add(product)
        db.session.commit()

        return redirect(url_for("products.index"))

    return render_template("products/add.jinja")


@products_bp.route("/<int:id>", methods=["GET", "POST"])
def each(id):
    product = Product.query.get_or_404(id)
    if request.method == "POST":

        db.session.delete(product)
        db.session.commit()

        return redirect(url_for("products.index"))

    return render_template("products/each.jinja", product=product)


@products_bp.route("/<int:id>/edit", methods=["GET", "POST"])
def edit(id):
    product = Product.query.get_or_404(id)
    if request.method == "POST":
        product.title = request.form["title"]
        product.description = request.form["description"]
        product.price = request.form["price"]

        db.session.add(product)
        db.session.commit()

        return redirect(url_for("products.each", id=product.id))

    return render_template("products/edit.jinja", product=product)
