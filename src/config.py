class Config:
    SECRET_KEY = 'DentalClinicaNetwork_2000'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = '162.214.71.29'
    MYSQL_USER = 'wwdent_userfacturas'
    MYSQL_PASSWORD = ']Q]tWWf5n=Fj' 
    MYSQL_DB = 'wwdent_facturacion'

config = {
    'development': DevelopmentConfig  # Corregido 'DevelopmnetConfig' a 'DevelopmentConfig'
}
