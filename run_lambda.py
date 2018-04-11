from flask_lambda import FlaskLambda
from app import create_app


http_server = create_app(FlaskLambda)
