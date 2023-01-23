bash:
	docker-compose exec donate_ukraine bash -c "export COLUMNS=`tput cols`; export LINES=`tput lines`; exec bash"

shell:
	docker-compose exec donate_ukraine /code/manage.py shell

superuser:
	docker-compose exec donate_ukraine /code/manage.py createsuperuser  --username=root --password=12345678

migrations:
	docker-compose exec donate_ukraine /code/manage.py makemigrations
#	docker-compose exec donate_ukraine /code/manage.py makemigrations lots
#	docker-compose exec donate_ukraine /code/manage.py makemigrations users
#	docker-compose exec donate_ukraine /code/manage.py makemigrations storage
#	docker-compose exec donate_ukraine /code/manage.py makemigrations monobank


migrate:
	docker-compose exec donate_ukraine /code/manage.py migrate
#	docker-compose exec donate_ukraine /code/manage.py migrate donate_ukraine
#	docker-compose exec donate_ukraine /code/manage.py migrate monobank
#	docker-compose exec donate_ukraine /code/manage.py migrate storage
#	docker-compose exec donate_ukraine /code/manage.py migrate users
	# Works for Windows:
	# docker-compose exec donate_ukraine python manage.py migrate

drop-db:
	docker-compose exec donate_ukraine /code/manage.py flush

build:
	docker build . -t donate_ukraine

run:
	echo 'DON`T FORGET TO CHANGE SECRET KEY BEFORE FINAL DEPLOY'
	sleep 2
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
