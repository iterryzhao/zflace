from flask import Flask

app = Flask(__name__)

# Loading config file, config.py must be under the root folder of project
app.config.from_object('config')

from app import views