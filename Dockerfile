FROM python:3.6
COPY . /usr/app
ENV FLASK_APP=main.py
WORKDIR /usr/app
RUN pip install -r requirements.txt
ENTRYPOINT ["flask","run"]
