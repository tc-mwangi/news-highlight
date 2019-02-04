import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    test class to test Article class
    '''

    def setUp(self):
        '''
        set up method to run before every test
        '''
        self.new_article = Article("Dan Merica, CNN", "Pressure intensifies on Northam to resign as key allies pull their support", "Pressure is mounting on Virginia Democratic Gov. Ralph Northam to resign.", "http://us.cnn.com/2019/02/01/politics/democrats-call-on-northam-to-resign/index.html", "https://cdn.cnn.com/cnnnext/dam/assets/190201165929-01-northam-blackface-photo-super-tease.jpg", "2019-02-02T15:50:33Z", "(CNN)Pressure is mounting on Virginia Democratic Gov. Ralph Northam to resign.\r\nNortham, who apologized earlier Friday for appearing in a racist yearbook photo showing one person dressed in blackface and another in the Ku Klux Klan's signature white hood and … [+12150 chars]"   )


    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Article))

# "author": "Dan Merica, CNN",
# "title": "Pressure intensifies on Northam to resign as key allies pull their support",
# "description": "Pressure is mounting on Virginia Democratic Gov. Ralph Northam to resign.",
# "url": "http://us.cnn.com/2019/02/01/politics/democrats-call-on-northam-to-resign/index.html",
# "urlToImage": "https://cdn.cnn.com/cnnnext/dam/assets/190201165929-01-northam-blackface-photo-super-tease.jpg",
# "publishedAt": "2019-02-02T15:50:33Z",
# "content": "(CNN)Pressure is mounting on Virginia Democratic Gov. Ralph Northam to resign.\r\nNortham, who apologized earlier Friday for appearing in a racist yearbook photo showing one person dressed in blackface and another in the Ku Klux Klan's signature white hood and … [+12150 chars]"


