from flask import Flask, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_talisman import Talisman
from html_sanitizer import Sanitizer


# Import Blueprints
from .home.home import home
from .auth.auth import auth
from .profile.profile import profile
from .cart.cart import cart
from .product.product import product
from .order.order import order


# Extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
bcrypt = Bcrypt()
talisman = Talisman()
sanitizer = Sanitizer()


# Callback function for flask_login
@login_manager.user_loader
def load_user(user_id):
    from db_helper import get_user
    from models import User
    return get_user(User.id == user_id)


# Talisman CSP config
csp = {
    'default-src': ["'self'"],
    'font-src': ["'self'", 'https://cdnjs.cloudflare.com', 'https://fonts.gstatic.com'],
    'script-src': ["'self'", 'https://cdnjs.cloudflare.com'],
    'style-src': ["'self'", 'https://cdnjs.cloudflare.com'],
    'img-src': ["'self'"]
}


# App
def create_app():
    app = Flask(__name__, instance_relative_config=False)

    # Config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
    app.config['SECRET_KEY'] = 'jLT9w0VIScCRXXPRwuWb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialization
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    talisman.init_app(
            app,
            content_security_policy=csp,
            force_https=False
        )

    # Middleware to sanitize Html request
    @app.before_request
    def before_request():
        if request.method == 'POST':
            try:
                from utils import sanitize_input
                request.form = sanitize_input(request.form)
            except Exception as e:
                return f"Error: {e}", 400

    with app.app_context():
        # Import Models
        import models

        # Create DB
        # from utils import db_setup
        # from data import insert
        # db_setup('ecommerce.sql')
        # print(insert())

        # Register Blueprints
        app.register_blueprint(home, url_prefix='/home')
        app.register_blueprint(auth, url_prefix='/auth')
        app.register_blueprint(profile, url_prefix='/profile')
        app.register_blueprint(cart, url_prefix='/cart')
        app.register_blueprint(product, url_prefix='/product')
        app.register_blueprint(order, url_prefix='/order')

        # Index route
        @app.route('/')
        def index():
            return redirect(url_for("home.index"))

        return app
