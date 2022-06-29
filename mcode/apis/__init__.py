"""General controller for mcode apis."""
from mcode.apis import login


def register_routes(api):
    """Register all API's URL routes with the passed api object context."""
    # Login
    api.add_resource(login.LoginAPI, '/login/')
