#!/usr/bin/env python
# Module handling routing of requests from Flask app

from typing import Dict
from flask import current_app as app

def _default_index() -> str:
    """
    Default index
    """
    return "Hi"

def _name_page(name: str) -> str:
    """
    Name page
    """
    return f"Hi, {name}. Welcome to this website!"

routes: Dict = {
    "/": _default_index,
    "/naming/<name>": _name_page
}

def create_routes():
    """
    Create url rules and add to app
    """
    for page_name in routes:
        with app.app_context():
            app.add_url_rule(page_name, view_func=routes[page_name])