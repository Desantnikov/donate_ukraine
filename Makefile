bash:
	docker-compose exec donate_ukraine bash -c "export COLUMNS=`tput cols`; export LINES=`tput lines`; exec bash"

shell:
	docker-compose exec donate_ukraine /code/manage.py shell

superuser:
	docker-compose exec donate_ukraine /code/manage.py createsuperuser  --username=root --password=12345678

migrations:
	docker-compose exec donate_ukraine /code/manage.py makemigrations

migrate:
	docker-compose exec donate_ukraine /code/manage.py migrate

drop-db:
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
	docker-compose exec donate_ukraine pytest .

# -------------------- HEROKU COMMANDS -------------

heroku-bash:
	heroku run bash

heroku-shell:
	heroku run python ./manage.py shell

heroku-superuser:
	python ./manage.py createsuperuser  --username=root --password=12345678

heroku-migrate:
	heroku run python ./manage.py migrate

heroku-drop-db:
	heroku run python ./manage.py flush
