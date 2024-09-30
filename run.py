from datetime import datetime
from flask import Flask, render_template
import json

from app import create_app

if __name__ == '__main__':
    app = create_app()
    try:
        app.secret_key = open('secret_key.txt', 'r').read().strip()
    except FileNotFoundError:
        raise FileNotFoundError("You need to create a file named 'secret_key.txt' and write a secret key in it.")

    try:
        with open('ip_and_port.txt', 'r') as f:
            IP, PORT = f.read().split(':')  # IP:PORT
    except FileNotFoundError:
        IP, PORT = 'localhost', '5000'

    app.run(host=IP, port=PORT, debug=True)