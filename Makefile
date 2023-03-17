bash:
	docker-compose exec donate_ukraine bash -c "export COLUMNS=`tput cols`; export LINES=`tput lines`; exec bash"

shell:
	docker-compose exec donate_ukraine /code/manage.py shell_plus

superuser:
	docker-compose exec donate_ukraine /code/manage.py createsuperuser  --username=root --password=12345678 --first_name=John --last_name=Doe --phone_number=+380667829374

migrations:
	docker-compose exec donate_ukraine /code/manage.py makemigrations

migrate:
	docker-compose exec donate_ukraine /code/manage.py migrate

clear-db:
	docker-compose exec donate_ukraine /code/manage.py flush

build:
	docker build . -t donate_ukraine

run:
	docker-compose up

run-db:
	docker-compose up db

rebuild:
	docker-compose up --build --force-recreate --remove-orphans

fix-files-ownership:
	sudo chmod -R 777 postgres-data/  # TODO: fix issue with `postgres-data` folder permissions
	sudo chmod -R 777 ./lots/migrations/
	sudo chmod -R 777 ./storage/migrations/
	sudo chmod -R 777 ./monobank/migrations/
	sudo chmod -R 777 ./users/migrations/

tests:
	export DJANGO_SETTINGS_MODULE=settings.compose # why not working?
	docker-compose exec donate_ukraine pytest .

lint:
	isort .
	black .
	flake8 .

refresh-jars-data:
	docker-compose exec donate_ukraine python ./manage.py refresh_monobank_jars_data --delay=1
# -------------------- HEROKU COMMANDS -------------

heroku-logs:
	heroku logs --tail

heroku-bash:
	heroku run bash

heroku-shell:
	heroku run python ./manage.py shell

heroku-superuser:
	heroku run python ./manage.py createsuperuser  --username=root --password=12345678 --first_name=John --last_name=Doe --phone_number=+380667829374

heroku-migrate:
	heroku run python ./manage.py migrate

heroku-clear-db:
	heroku run python ./manage.py flush

heroku-dbshell:
	heroku run python ./manage.py dbshell
	# Drop schema:
	# DROP SCHEMA public CASCADE; CREATE SCHEMA public;
	# GRANT ALL ON SCHEMA public TO postgres; GRANT ALL ON SCHEMA public TO public;

heroku-restart-dyno:
	heroku dyno:restart

heroku-collectstatic:
	heroku run python ./manage.py collectstatic

heroku-refresh-jars-data:
	heroku run python ./manage.py refresh_monobank_jars_data --delay=1
