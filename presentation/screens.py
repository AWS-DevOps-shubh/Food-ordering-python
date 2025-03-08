# presentation/screens.py

from flask import Blueprint, render_template, request, redirect, url_for, current_app

screens_bp = Blueprint('screens_bp', __name__)

@screens_bp.route('/')
def index():
    # Home / front page
    return render_template('index.html')

@screens_bp.route('/menu')
def menu():
    # Retrieve the business logic from app config
    food_system = current_app.config['FOOD_SYSTEM']
    menu_items = food_system.get_menu()
    return render_template('menu.html', menu_items=menu_items)

@screens_bp.route('/add_item', methods=['POST'])
def add_item():
    item = request.form.get('item')
    if item:
        current_app.config['FOOD_SYSTEM'].add_item(item)
    return redirect(url_for('screens_bp.menu'))

@screens_bp.route('/order')
def order():
    food_system = current_app.config['FOOD_SYSTEM']
    order_summary = food_system.get_order_summary()
    total = food_system.get_total()
    return render_template('order.html', order_summary=order_summary, total=total)

@screens_bp.route('/remove_item', methods=['POST'])
def remove_item():
    item = request.form.get('item')
    if item:
        current_app.config['FOOD_SYSTEM'].remove_item(item)
    return redirect(url_for('screens_bp.order'))
