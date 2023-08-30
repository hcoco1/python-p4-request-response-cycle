#!/usr/bin/env python3
# The above line allows the script to be run as an executable in UNIX-like systems

# Import necessary libraries and modules
import os
from flask import Flask, request, current_app, g, make_response

# Create a new Flask web application
app = Flask(__name__)

# Register a function to run before each request
@app.before_request
def app_path():
    # Store the absolute path of the current working directory 
    # in the Flask global object 'g' so it's accessible in other views
    g.path = os.path.abspath(os.getcwd())

# Define the route for the root URL
@app.route('/')
def index():
    # Get the 'Host' header from the incoming HTTP request
    host = request.headers.get('Host')
    # Get the name of the current Flask application
    appname = current_app.name
    # Construct the HTML response body
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''
    # Define the HTTP status code for the response (200 means OK)
    status_code = 200
    # Define additional headers for the response (currently empty)
    headers = {}

    # Create and return the HTTP response with the constructed body, status code, and headers
    return make_response(response_body, status_code, headers)


if __name__ == '__main__':
    # Start the Flask development server on port 5555 with debugging enabled
    app.run(port=5555, debug=True)



