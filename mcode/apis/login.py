"""Login/Logout API."""
import json
import traceback
import datetime as dt

from flask import request
from flask_restful import Resource


def connection_data(request):
    headers_sent = json.dumps(
        request.environ['werkzeug.request'].headers.environ,
        indent=4,
        default=lambda o: '<not printable value>'
    )
    return {
        "trace": request.access_route,
        "client": request.environ['werkzeug.request'].user_agent.__dict__,
        "headers_sent": json.loads(headers_sent)
    }


class LoginAPI(Resource):
    """API for login."""

    def post(self):
        """Login user by app_ip, pwd and otp."""
        try:
            login_data = request.get_json()
            app_id = login_data.get('app_id', '')
            password = login_data.get('password', '')
            otp = login_data.get('otp', '')

            if False:
                # Real login logic here if pass validations
                pass
            else:
                # Log the problem in stdout
                print("User login failed!")
                print("Invalid password for ID: " + app_id)
                print("Invalid Token for ID: " + app_id)
                print("server time now is: " + (
                    dt.datetime.now().isoformat()
                ))

            return {
                'payload': request.get_json(),
                'connection_data': connection_data(request)

            }
        except Exception:
            traceback.print_exc()

        return {'message': 'User login failed!'}, 404
