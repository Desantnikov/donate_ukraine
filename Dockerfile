#FROM python:3.9-slim
#
#ENV PYTHONPATH=/code
#
#

#
#RUN apt-get update
#RUN apt-get install -y --no-install-recommends libpq-dev python3-dev gcc python3-dev
#RUN pip3 install --upgrade pip
#RUN pip3 install pipenv psycopg2-binary
#
#
#
#
#RUN pipenv install --system --deploy --ignore-pipfile
#
#CMD ["python3", "manage.py", "migrate"]
#
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
#
#
#


#FROM ubuntu:16.04
FROM python:3.9-slim

COPY . /code
WORKDIR /code

RUN apt-get update
#RUN apt-get -y install libpq-dev python3-dev gcc python3-dev
RUN apt-get install -y --no-install-recommends libpq-dev python3-dev gcc python3-dev
RUN pip3 install --upgrade pip
RUN pip3 install pipenv
RUN pipenv install --system --deploy

#COPY base.py base.py
ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]