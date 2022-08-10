from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False,
                template_folder='../build',
                static_folder='../build/static'
                )

    app.config.from_object('config.Config')
    with app.app_context():

        from .properties.properties import properties
        from .properties_list.properties_list import properties_list

        app.register_blueprint(properties)
        app.register_blueprint(properties_list)

        return app
