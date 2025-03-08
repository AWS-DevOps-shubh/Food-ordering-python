# main.py
from flask import Flask
from business.food_ordering_system import FoodOrderingSystem
from presentation.screens import screens_bp

def create_app():
    app = Flask(__name__, 
                template_folder="presentation/templates", 
                static_folder="presentation/static")
    

    # Instantiate the business logic
    food_system = FoodOrderingSystem()

    # Store our business logic in the app config
    app.config['FOOD_SYSTEM'] = food_system

    # Register our “presentation” blueprint
    app.register_blueprint(screens_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", debug=True)
