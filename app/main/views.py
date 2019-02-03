from flask import render_template, request, redirect, url_for
# from app import app
from . import main
from ..requests import get_source



#  views
@main.route('/')
def index():
	'''
	function returns index page and its data
	'''
	# Getting sources
	news_sources = get_source('sources')
	print(news_sources)
	title = 'WithIt- Get current news.'
	
	
	return render_template('index.html', title = title, sources = news_sources)
	