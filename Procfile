# when calling a django process, a django settings file needs to be set
# in the DJANGO_SETTINGS_MODULE environment variable.
# the django settings file heroku uses is stored as a config var within heroku

# command to run the web application
# --preload helps speed up heroku dyno boot times
web: gunicorn event_aggregator.wsgi --preload

# command to be run on releases.
# heroku calls collectstatic on django apps, so we don't have to call it here
release: python manage.py migrate