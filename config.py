class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'Rcris.mysql.pythonanywhere-services.com'
    MYSQL_USER = 'Rcris'
    MYSQL_PASSWORD = 'p6QZ)N9pe2uMn_m'
    MYSQL_DB = 'Rcris$default'


config = {
    'development': DevelopmentConfig
}
