migrations:
		docker-compose exec donate_ukraine /code/manage.py makemigrations

migrate:
		docker-compose exec donate_ukraine /code/manage.py migrate

