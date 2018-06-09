FROM python:3.6
COPY requirements.txt /usr/app/requirements.txt

WORKDIR /usr/app
RUN pip install -r requirements.txt

COPY . /usr/app

ENV FLASK_APP=main.py
ENV FLASK_ENV=development
ENTRYPOINT ["flask","run","-h","0.0.0.0","-p","80"]
