FROM python:3.6
RUN apt-get update
RUN apt-get install -y nginx supervisor
COPY requirements.txt /usr/app/requirements.txt

WORKDIR /usr/app
RUN pip install -r requirements.txt

COPY . /usr/app

RUN rm /etc/nginx/sites-enabled/default
COPY docker-deps/supervisor.conf /etc/supervisor/conf.d/supervisor.conf
COPY docker-deps/ebay.conf /etc/nginx/sites-enabled/ebay.conf

ENV FLASK_ENV=production

ENTRYPOINT ["supervisord", "-n"]
