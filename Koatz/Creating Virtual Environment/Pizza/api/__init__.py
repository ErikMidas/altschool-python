from flask import Flask
from flask_restx import Api
from .orders.views import order_namespace
from .auth.views import auth_namespace
from .config.config import config_dict
from .utils import db
from .models.orders import Order
from .models.users import User
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_jwt_extended.exceptions import JWTExtendedException
from werkzeug.exceptions import NotFound, MethodNotAllowed

def create_app(config=config_dict["dev"]):
    app = Flask(__name__)
    
    app.config.from_object(config)
    
    db.init_app(app)
    
    jwt = JWTManager(app)

    migrate = Migrate(app, db)
    
    authorizations = {
        "Bearer Auth": {
            "type": "apiKey",
            "in": "header",
            "name": "Authorization",
            "description": "Add a JWT token to the header with ** Bearer &lt;JWT&gt; token to authorize **"
        }
    }

    api = Api(
        app,
        title="Pizzerra Pizza Delivery API",
        description="A simple pizza delivery REST API",
        # version=1.3,
        authorizations=authorizations,
        security="Bearer Auth",
        contact_email="koats14@gmail.com"
        )

    api.add_namespace(order_namespace)
    api.add_namespace(auth_namespace)
    
    @api.errorhandler(NotFound)
    def not_found(error):
        return {"error": "Not Found"}, 404
    
    @api.errorhandler(MethodNotAllowed)
    def method_not_allowed(error):
        return {"error": "Method Not Allowed"}, 404
    
    @api.errorhandler(JWTExtendedException)
    def handle_jwt_exceptions(error):
        return {"message": str(error)}, getattr(error, "code", 401)
    
    @app.shell_context_processor
    def make_shell_context():
        return {
            "db": db,
            "User": User,
            "Order": Order 
        }
    
    return app
