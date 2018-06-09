NAME="flask"
VERSION=`cat VERSION`
REGION="eu-west-1"
AWS_ACCOUNT="206636293913"
run:
	. .virtualenv/bin/activate; FLASK_APP=main.py flask run

docker-build:
	docker build -t flask:develop .

docker-run:
	docker run -it -p 5000:5000 flask:develop

docker-login:
	aws  --profile michalbagrowski ecr get-login --no-include-email --region $(REGION)

version:
	docker build -t flask-$(REGION):$(VERSION) .
	docker tag flask-$(REGION):$(VERSION) $(AWS_ACCOUNT).dkr.ecr.$(REGION).amazonaws.com/flask-$(REGION):$(VERSION)
	docker push $(AWS_ACCOUNT).dkr.ecr.$(REGION).amazonaws.com/flask-$(REGION):$(VERSION)

bump:
	. .virtualenv/bin/activate; python scripts/bump.py

.PHONY: version
