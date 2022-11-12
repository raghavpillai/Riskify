#!/usr/bin/env python
# Main script handling instantiation and creation of webserver and functionality

import src.app as App
import src.routing as Router

def create_server() -> None:
    """
    Initialization and creation of web server and routing
    """
    App.create_app()
    print("Initialized app")

    Router.create_routes()
    print("Created routes")

    print("Running app")
    App.run_app(True)
        

if __name__ == '__main__': 
    create_server()