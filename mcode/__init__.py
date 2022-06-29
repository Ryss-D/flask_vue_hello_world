"""Main root module."""

from flask import Flask
from flask_restful import Api

# Explicit instantiate the plugins modules
# before mcode modules are imported because they depends on.

api = Api(prefix="/api")


def mcode_factory():
    """Return the MCODE FLASK APP.

    It is configured as an instance of a Flask application.
    """
    mcode_app = Flask(__name__)

    with mcode_app.app_context():

        # Import my app modules with its implicit recursive imports
        from . import controllers

        # Flask restfull
        # API's routes must be registered within the app context
        from . import apis
        apis.register_routes(api)
        api.init_app(mcode_app)

    return mcode_app
