# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 14:01:08 2025

@author: Timo Gandalo
"""

from flask import Flask, render_template




app = Flask(__name__)



@app.route('/home', methods = ['GET', 'POST'])
def principal():
   
    return render_template('base.html')

app.run(host='localhost',  port = 8080)