LAUNCH TESTS FROM INSODE THE CONTAINER

make bash
pytest .


To deploy on heroku
heroku config:set DJANGO_SETTINGS_MODULE=settings.heroku

Migrations on heroku
heroku run python manage.py migrate
heroku run python manage.py createsuperuser


####
DATABASE SECTION HAS TO BE UNCOMMENTED BEFORE DEPLOY

SECRET KEY HAS TO BE CHANGED BEFORE FINAL DEPLOY
