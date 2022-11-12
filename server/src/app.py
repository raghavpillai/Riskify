#!/usr/bin/env python
# Main 

from flask import Flask
from flask import current_app as app

"""
Module creating and running the Flask application
"""

def run_app(is_debug: bool=False) -> None:
    """
    Run flask app
    @param is_debug (bool): If flask runs in debug mode
    """
    app.run(debug=is_debug)

def create_app() -> None:
    app_obj = Flask(__name__)
    app_obj.app_context().push()