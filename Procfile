# command to run the web application
# --preload helps speed up heroku dyno boot times
web: gunicorn bakeronomicon.wsgi --preload

# command to be run on releases.
# heroku calls collectstatic on django apps, so we don't have to call it here
release: python manage.py migrate