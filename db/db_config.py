from helpers import get_env_variable


# POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_URL = get_env_variable("DATABASE_URL")
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")
# POSTGRES_DB = get_env_variable("POSTGRES_DB")

DB_URL = POSTGRES_URL
'postgres://sjdhznffdawcts:fc3f1970bc27a0caf4290759b8baf3c8087b73902b88b06d9ee98fb3d8135b10@ec2-52-23-14-156.compute-1.amazonaws.com:5432/d62nrfbfi9i5hl'



SQLALCHEMY_DATABASE_URI = DB_URL
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = 'some-secret-string'

