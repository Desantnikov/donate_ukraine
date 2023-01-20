LAUNCH TESTS FROM INSODE THE CONTAINER

make bash
pytest .


To deploy on heroku
heroku config:set DJANGO_SETTINGS_MODULE=settings.settings
