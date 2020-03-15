from helpers import get_env_variable

# POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_URL = get_env_variable("DATABASE_URL")
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")
# POSTGRES_DB = get_env_variable("POSTGRES_DB")

DB_URL = 'postgres://voheseigswrsbm:cc68d8363f89bddabbe1ce4735a7020217b0f96c229854316aaf7592e7fd385c@ec2-3-234-169-1' \
         '47.compute-1.amazonaws.com:5432/d97uq4qkakfic0'

SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'some-secret-string'
