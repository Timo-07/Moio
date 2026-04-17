# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 14:01:08 2025

@author: Timo Gandalo
"""

from flask import Flask, render_template, flash, request
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import Form
import os



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:gandalo@127.0.0.1/cordas'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class tb_role(db.Model):
    IdRole = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable = False)
    def __repr__(self):
        return f'<Usuario{self.nome}>'
class tb_pessoa(db.Model):
    IdPessoa = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(100), nullable = False)
    def __repr__(self):
        return f'<Usuario{self.nome}>'
class tb_user(db.Model):
    IdUser = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), nullable = False)
    PASSWORD = db.Column(db.String(100), nullable = False)
    IdRole = db.Column(db.Integer,db.ForeignKey(tb_role.IdRole),nullable=False)
    def __repr__(self):
        return f'<Usuario{self.nome}>'

@app.route('/u', methods = ['GET', 'POST'])
def principal():
    if request.form:
        user = tb_pessoa(Nome = request.form.get("nome"))
        db.session.add(user)
        db.session.commit()
    pessoa = tb_pessoa.query.all()
    return render_template('base.html', pessoa=pessoa)
@app.route('/user')
def add_user():
    novo = tb_role(nome = "h")
    db.session.add(novo)
    db.session.commit()
    return 'Usuario Adionado!!'
@app.route('/',  methods = ['GET', 'POST'])
def add_usuario():
    if request.form:
        novo = tb_user(nome = request.form.get("nome"),email = request.form.get("email"), PASSWORD = request.form.get("PASSWORD"),IdRole = request.form.get("IdRole"))
        db.session.add(novo)
        db.session.commit()
    pessoa = db.session.query(tb_role.IdRole).all()
    return render_template('base.html', pessoa = pessoa)
app.run(host='localhost',  port = 8080)