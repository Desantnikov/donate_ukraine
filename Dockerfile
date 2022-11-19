FROM python:3.9-slim

COPY . /code
WORKDIR /code

RUN apt-get update
RUN apt-get install -y --no-install-recommends libpq-dev python3-dev gcc python3-dev
RUN pip3 install --upgrade pip
RUN pip3 install pipenv
RUN pipenv install --system --deploy

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]