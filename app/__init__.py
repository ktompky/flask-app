from flask import Flask, render_template, flash, request
from config import Config


# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(Config)



from app import routes
