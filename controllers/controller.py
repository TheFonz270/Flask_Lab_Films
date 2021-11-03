from app import app
from flask import render_template
from models.orders_made import orders_list

@app.route('/')
def index():
    return render_template('index.html', orders_list=orders_list)

@app.route('/order/<i>')
def order(i):
    n=int(i)
    return render_template('order.html', order=orders_list[n])