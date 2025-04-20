from flask import Blueprint, request, jsonify
from .models import Product
from .schemas import ProductSchema
from . import db

api_blueprint = Blueprint('api', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@api_blueprint.route("/products", methods=["POST"])
def add_product():
    data = request.json
    new_product = product_schema.load(data)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product), 201

@api_blueprint.route("/products", methods=["GET"])
def get_all_products():
    products = Product.query.all()
    return products_schema.jsonify(products)

@api_blueprint.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = Product.query.get_or_404(id)
    return product_schema.jsonify(product)

@api_blueprint.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.json
    for field in ['name', 'quantity', 'price']:
        if field in data:
            setattr(product, field, data[field])
    db.session.commit()
    return product_schema.jsonify(product)

@api_blueprint.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return '', 204
