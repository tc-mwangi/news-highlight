from flask import render_template, request, redirect, url_for
# from app import app
from . import main
from ..requests import get_source, get_article


#  views
@main.route('/')
def index():
	'''
	function returns index page and its data
	'''

	title = 'WithIt- Get current news.'
	# Getting sources
	news_sources = get_source('sources')
	print(news_sources)

	# Getting top news
	news_articles = get_article('articles')
	print(news_articles)

	
	return render_template('index.html', title = title, sources = news_sources, articles = news_articles)
	