release: python3 manage.py makemigrations
release: python3 manage.py migrate
web: gunicorn profiles_project.wsgi --log-file -