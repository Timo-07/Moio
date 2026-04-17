# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 14:01:08 2025

@author: Timo Gandalo
"""

from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def principal():
    return render_template('base.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render usa variável PORT
    app.run(host="0.0.0.0", port=port)