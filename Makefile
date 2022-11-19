bash:
	docker-compose exec donate_ukraine bash -c "export COLUMNS=`tput cols`; export LINES=`tput lines`; exec bash"

shell:
	docker-compose exec donate_ukraine /code/manage.py shell

createsuperuser:
	docker-compose exec donate_ukraine /code/manage.py createsuperuser

migrations:
	docker-compose exec donate_ukraine /code/manage.py makemigrations
	docker-compose exec donate_ukraine /code/manage.py makemigrations donate_ukraine

migrate:
	docker-compose exec donate_ukraine /code/manage.py migrate
	docker-compose exec donate_ukraine /code/manage.py migrate donate_ukraine

drop-db:
	docker-compose exec donate_ukraine /code/manage.py flush

populate-db:
	docker-compose exec donate_ukraine /code/manage.py populate_data

recreate-db:
	docker-compose exec donate_ukraine /code/manage.py flush
	docker-compose exec donate_ukraine /code/manage.py populate_data

build:
	docker build . -t donate_ukraine

run:
	docker-compose up

rebuild:
	docker-compose up --build --force-recreate --remove-orphans

fix-files-ownership:
	sudo chown -R a.desiatnykov postgres-data/  # TODO: fix issue with `postgres-data` folder permissions
	sudo chown -R a.desiatnykov ./donate_ukraine/migrations/
