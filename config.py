import os

class Config:
  '''
  general configaration class
  NEWS_API_BASE_URL = ''
  NEWS_API_KEY = ''
  '''


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


  

 

