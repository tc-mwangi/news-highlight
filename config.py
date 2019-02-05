import os

class Config:
  '''
  general configaration class
  '''
  NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?language=en&apiKey={}'
  NEWS_API_KEY = 'dfc2defa711d4fb4bd3a57b7da3c9a62'
  NEWS_API_BASE_URL2 = 'https://newsapi.org/v2/top-headlines?language=en&apiKey={}'
  NEWS_API_BASE_URL3 = 'https://newsapi.org/v2/top-headlines?sources={}language=en&apiKey={}'

#   top-headlines?language=en
#   NEWS_API_BASE_URL = 'https://newsapi.org/v2/{}?apiKey={}'
#   NEWS_API_KEY = 'dfc2defa711d4fb4bd3a57b7da3c9a62'

    
    
# https://newsapi.org/v2/sources?apiKey=dfc2defa711d4fb4bd3a57b7da3c9a62
# https://newsapi.org/v2/top-headlines?sources=cnn&apiKey=dfc2defa711d4fb4bd3a57b7da3c9a62
    

class ProdConfig(Config):
    '''
    production configuration class
    '''
    pass


class DevConfig(Config):
    '''
    development configuration class
    '''
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}


  

 

