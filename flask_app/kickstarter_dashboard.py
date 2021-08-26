from flask import Flask, request, render_template
from flask_app.predict import kickstarter_prediction

app = Flask(__name__)