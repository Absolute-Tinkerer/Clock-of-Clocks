# -*- coding: utf-8 -*-
"""
Created on Fri May 21 10:38:35 2021

@author: The Absolute Tinkerer
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    try:
        # Start the server
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        print(e)
