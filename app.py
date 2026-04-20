from flask import Flask, request, render_template_string
from markupsafe import escape
from werkzeug.utils import secure_filename
import sqlite3
import subprocess
import requests
import os

app = Flask(__name__)
app.secret_key = "DEADC0DE"

@app.route('/')
def index():
    return """<h1>Snyk & Colgate - Find and Fix Lab</h1>"""

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    query = f"SELECT username FROM users WHERE id = {user_id}"
    cur.execute(query)
    result = cur.fetchone()
    return f"User: {result}" if result else "User not found"

@app.route('/hello')
def hello():
    name = request.args.get('name', 'Guest')
    return f"<h1>Hello {name}</h1>"

@app.route('/network/ping')
def ping_server():
    hostname = request.args.get('host')
    cmd = f"ping -c 1 {hostname}"
    output = subprocess.check_output(cmd)
    return f"<pre>{output.decode()}</pre>"

@app.route('/view-log')
def view_log():
    file_path = request.args.get('file')
    with open(file_path, 'r') as f:
        return f.read()

if __name__ == "__main__":
    app.run(debug=True, port=5001)
