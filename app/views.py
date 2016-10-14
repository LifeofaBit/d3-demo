from flask import render_template, flash, redirect
from app import app

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/intro')
def intro():
	return render_template('intro.html')

@app.route('/mon')
def mon():
	return render_template('mon.html', title="Pokemon Data")

@app.route('/stream')
def stream():
	return render_template('stream.html', title="Streaming Viz Examples")
