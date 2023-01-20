LAUNCH TESTS FROM INSODE THE CONTAINER

make bash
pytest .


To deploy on heroku
heroku config:set DJANGO_SETTINGS_MODULE=settings.settings

Migrations on heroku
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
