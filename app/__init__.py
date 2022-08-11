from flask import Flask


def create_app():
    app = Flask(__name__,)

    app.config.from_object('config.Config')
    with app.app_context():

        from .property.property import property_profile
        from .home.home import home

        app.register_blueprint(property_profile)
        app.register_blueprint(home)

        return app
