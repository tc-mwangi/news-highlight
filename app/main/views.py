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

# display articles by source
@main.route('/sources/<int:id>')
def show_articles(id):
    '''
    View articles page function that returns articles from a selected source
    '''
    articles = show_articles(id)
    
    return render_template('article.html', articles = articles)


# search for articles according to source name
# @main.route('/search/<source_name>')
# def search(source_name):
#     '''
#     View function to display the search results
#     '''
#     movie_name_list = movie_name.split(" ")
#     movie_name_format = "+".join(movie_name_list)
#     searched_movies = search_movie(movie_name_format)
#     title = f'search results for {movie_name}'

#     return render_template('search.html', movies = searched_movies)

# get articles by source name view
# @main.route('/movie/<movie_id>')
# def movie(movie_id):
#     '''
#     view movie page that returns the details of a particular movie and its data.
#     '''
#     movie = get_movie(id)
#     title = f'{ movie.title }'
#     reviews = Review.get_reviews(movie.id)

#     return render_template('movie.html', title = title, movie = movie, reviews = reviews)


# search for articles according to source name
# @main.route('/search/<movie_name>')
# def search(movie_name):
#     '''
#     View function to display the search results
#     '''
#     movie_name_list = movie_name.split(" ")
#     movie_name_format = "+".join(movie_name_list)
#     searched_movies = search_movie(movie_name_format)
#     title = f'search results for {movie_name}'

#     return render_template('search.html', movies = searched_movies)