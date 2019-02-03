import unittest
from app.models import Source

class SourceTest(unittest.TestCase):
    '''
    test class to test Source class
    '''

    def setUp(self):
        '''
        set up method to run before every test
        '''
        self.new_source = Source("abc-news", "ABC News", "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.", "https://abcnews.go.com", "general", "en", "us" )


    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Source))


# -"sources": [
# -{
# "id": "abc-news",
# "name": "ABC News",
# "description": "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com.",
# "url": "https://abcnews.go.com",
# "category": "general",
# "language": "en",
# "country": "us"
# },