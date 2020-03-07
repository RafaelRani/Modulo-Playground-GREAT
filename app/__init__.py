from flask import Flask, url_for, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
import json, random

app = Flask(__name__)

from app.controllers import login
from app.controllers import default
