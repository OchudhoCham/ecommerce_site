from flask import Flask, render_template, request, redirect, url_for
from models import Product

app = Flask(__name__)

# Dummy data for products (this can later be integrated with a database)
products = [
    {'id': 1, 'name': 'Laptop', 'price': 800, 'description': 'A high-performance laptop'},
    {'id': 2, 'name': 'Smartphone', 'price': 500, 'description': 'A powerful smartphone'},
    {'id': 3, 'name': 'Headphones', 'price': 150, 'description': 'Noise-cancelling headphones'}
]

@app.route('/')
def home():
    return render_template('home.html', products=products)

@app.route('/product/<int:id>')
def product_detail(id):
    product = next((prod for prod in products if prod['id'] == id), None)
    if product:
        return render_template('product_detail.html', product=product)
    return "Product not found", 404

@app.route('/cart')
def cart():
    return "Cart Page"

@app.route('/checkout')
def checkout():
    return "Checkout Page"

if __name__ == '__main__':
    app.run(debug=True)
