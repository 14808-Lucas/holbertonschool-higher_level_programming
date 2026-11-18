#!/usr/bin/env python3
"""Flask app that displays products from JSON, CSV or SQLite."""
import csv
import json
import sqlite3

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/items')
def items():
    """Read items from items.json and render them as a list."""
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
        items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []
    return render_template('items.html', items=items_list)


def read_json(filename):
    """Return the list of products stored in a JSON file."""
    with open(filename, 'r') as file:
        return json.load(file)


def read_csv(filename):
    """Return the list of products stored in a CSV file."""
    products = []
    with open(filename, 'r', newline='') as file:
        for row in csv.DictReader(file):
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products


def read_sql(filename):
    """Return the list of products stored in a SQLite database."""
    conn = sqlite3.connect(filename)
    try:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        return [dict(row) for row in cursor.fetchall()]
    finally:
        conn.close()


@app.route('/products')
def products():
    """Display products from the source given in the query string."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json('products.json')
    elif source == 'csv':
        data = read_csv('products.csv')
    elif source == 'sql':
        try:
            data = read_sql('products.db')
        except sqlite3.Error:
            return render_template('product_display.html',
                                   error="Database error")
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None:
        data = [p for p in data if str(p['id']) == product_id]
        if not data:
            return render_template('product_display.html',
                                   error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
