from flask import render_template, request, redirect, url_for
# from app import app
from . import main
from ..requests import get_source, get_article


#  views
@main.route('/')
def index():
	'''
	function returns homepage and its data
	'''

	title = 'WithIt- Get current news.'
	# Getting sources
	news_sources = get_source('sources')
	print(news_sources)

	return render_template('source.html', title = title, sources = news_sources)


@main.route('/article')
def article():
	'''
	function returns news article and its data
	'''
	news_articles = get_article('articles')
	print(news_articles)
    

	return render_template('article.html', articles = news_articles)

@main.route('/search')
def search():
	'''
	function returns source search results
	'''
	
	return render_template('search.html')


@main.route('/favourite')
def favourite():
	'''
	function returns users favourite news sources
	'''
	return render_template('favourite.html')


@main.route('/contact')
def contact():
	'''
	function returns users favourite news sources
	'''
	return render_template('contact.html')


