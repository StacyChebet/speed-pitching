from flask import Flask
from flask_bootstrap import flask_bootstrap

#Initializing application
app = Flask(__name__)

from app import views