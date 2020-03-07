from flask import Flask, url_for, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
import json, random
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(80))

	def __init__(self, username, password):
		self.username = username
		self.password = password


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def home():
	if not session.get('logged_in'):
		return render_template('index.html')
	else:
		if request.method == 'POST':
			username = getname(request.form['username'])
			#return render_template('menu2.html', data=getfollowedby(username))
			return redirect(url_for('playground', data=getfollowedby(username)))
		return redirect(url_for('playground'))


@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		return render_template('index.html')
	else:
		name = request.form['username']
		passw = request.form['password']
		try:
			data = User.query.filter_by(username=name, password=passw).first()
			if data is not None:
				session['logged_in'] = True
				session['user'] = name
				return redirect(url_for('home'))
			else:
				return render_template('index.html', msg="Usuário ou senha incorreto!")
		except:
			return render_template('index.html', msg="Usuário ou senha incorreto!")

@app.route('/register/', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		new_user = User(username=request.form['username'], password=request.form['password'])
		db.session.add(new_user)
		db.session.commit()
		return render_template('register.html', msg="Registrado com sucesso!")
	return render_template('register.html', msg="")

@app.route('/logout')
def logout():
	session['logged_in'] = False
	return redirect(url_for('home'))
