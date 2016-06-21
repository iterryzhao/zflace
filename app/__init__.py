from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)

# Loading config file, config.py must be under the root folder of project
app.config.from_object('config')

from app import views

toolbar = DebugToolbarExtension(app)

# the toolbar is only enabled in debug mode:
app.debug = True
