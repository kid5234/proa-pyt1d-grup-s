from flask import Flask
import os
# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import route

SECRET_KEY = os.urandom(32)

# Load the config file
app.config.from_object('config')
app.config['SECRET_KEY'] = SECRET_KEY
