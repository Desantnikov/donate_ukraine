<h2>LAUNCH TESTS FROM INSODE THE CONTAINER</h2>

make bash
pytest .


<h2>To deploy on heroku</h2>
heroku config:set DJANGO_SETTINGS_MODULE=settings.heroku


<h2>S3 BUCKET SET PERMISSIONS BEFORE FINAL DEPLOY</h2>

# Delete this access key before final deploy
heroku config:set AWS_ACCESS_KEY_ID=<> AWS_SECRET_ACCESS_KEY=<> AWS_STORAGE_BUCKET_NAME=donate-ua-bucket
heroku config:set S3_BUCKET_NAME=donate-ua-bucket
heroku config:set DISABLE_COLLECTSTATIC=1

and make collectstatic manually with make heroku-collectstatic

heroku addons:create scheduler:standard

<h2>TO LAUNCH PROJECT</h2>
make run


<h2>TO LAUNCH TESTS IN PYCHARM</h2>

make run-db

<h3>Feel free to use aws keys from commit history, but pls note that they are no longer valid and bucket is deleted :D </h3>
