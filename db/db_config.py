from helpers import get_env_variable


# POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_URL = get_env_variable("DATABASE_URL")
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")
# POSTGRES_DB = get_env_variable("POSTGRES_DB")

# DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL,
                                      #                        db=POSTGRES_DB)

prefix = 'postgresql+psycopg2'

SQLALCHEMY_DATABASE_URI = prefix + POSTGRES_URL[8:]
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'some-secret-string'

