"""Log(In/Out) controller."""
from flask import (
    render_template,
    current_app as app
)


@app.route('/')
def identity_login():
    """Render login view."""
    return render_template('identity/login.html')
