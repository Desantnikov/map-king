web: gunicorn --worker-class eventlet -w 1 main:flask_app
init: python manage.py db init
migrate: python manage.py db migrate
upgrade: python manage.py db upgrade