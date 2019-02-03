from flask import render_template
# from app import app
from . import main


#  views
@main.route('/')
def index():
	'''
	function returns index page and its data
	'''
	return render_template('index.html')
	