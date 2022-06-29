"""Script to launch the mcode flask app."""
from mcode import mcode_factory


app = mcode_factory()

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
