#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

@app.route('/foo')
def foo():
    return '<h1>Milky Dog</h1>'

@app.route('/user/<username>')
def user(username: str):
    return f"<p>You are {username}</p>"


