
class config:
    SECRET_KEY='rocketsKoders2022'
    
class DevelopmentConfig(config):
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='root'
    MYSQL_PASSWORD=''
    MYSQL_DB='tienda_comics'
    
        
config={
    "development":DevelopmentConfig,
    "default":DevelopmentConfig
}
    