from flask import Blueprint, render_template

# Create a blueprint
main = Blueprint('main', __name__)

# Define routes as usual but within the blueprint

@main.route('/')
def start():
    # redirect to the home page with english language
    return "Welcome to the home page", 200