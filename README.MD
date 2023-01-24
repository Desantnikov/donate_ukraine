LAUNCH TESTS FROM INSODE THE CONTAINER

make bash
pytest .


To deploy on heroku
heroku config:set DJANGO_SETTINGS_MODULE=settings.heroku


S3 BUCKET SET PERMISSIONS BEFORE FINAL DEPLOY

# Delete this access key before final deploy
heroku config:set AWS_ACCESS_KEY_ID=AKIA3YGD4DJ7WJK3XM7X AWS_SECRET_ACCESS_KEY=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
heroku config:set S3_BUCKET_NAME=donate-ua-bucket
heroku config:set DISABLE_COLLECTSTATIC=1

and make collectstatic manually with make heroku-collectstatic
