def create_app(Flask):
    # Flask takes name of directory of app source code as argument
    app = Flask(__name__)

    app.config.from_object('config.default')
    # do not throw error if environment variable not set
    app.config.from_envvar('APP_CONFIG_FILE', silent=True)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    return app
