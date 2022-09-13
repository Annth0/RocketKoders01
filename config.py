
class config:
    SECRET_KEY='rocketsKoders2022'
    
class DevelopmentConfig(config):
    DEBUG=True
    
config={
    "development":DevelopmentConfig,
    "default":DevelopmentConfig
}
    