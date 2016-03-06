__author__ = 'Cloud'
from flask import Blueprint

bp = Blueprint('base', __name__)

from . import views
