from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False,
                template_folder='../build',
                static_folder='../build/static'
                )

    app.config.from_object('config.Config')
    print(app.config)
    with app.app_context():

        from .property.property import property_profile
        from .properties_list.properties_list import home

        app.register_blueprint(property_profile)
        app.register_blueprint(home)

        return app
