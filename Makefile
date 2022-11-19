bash:
		docker-compose exec donate_ukraine bash -c "export COLUMNS=`tput cols`; export LINES=`tput lines`; exec bash"

shell:
		docker-compose exec donate_ukraine /code/manage.py shell

migrations:
		docker-compose exec donate_ukraine /code/manage.py makemigrations

migrate:
		docker-compose exec donate_ukraine /code/manage.py migrate

run:
	docker-compose up

rebuild:
	docker-compose up --build --force-recreate --remove-orphans