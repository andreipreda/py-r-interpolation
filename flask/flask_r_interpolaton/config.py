class Config(object):
    DEBUG = True
    R_LOCATION = '../r_script'

class ProdConfig(Config):
    DEBUG = False
