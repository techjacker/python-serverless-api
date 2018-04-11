from flask import Flask
from app import create_app


http_server = create_app(Flask)
