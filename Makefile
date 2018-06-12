NAME="flask"
VERSION=`cat VERSION`
REGION="us-east-1"
AWS_ACCOUNT="206636293913"
CLOUDFRONT_ID="E3V1JSQA1HZG36"
run:
	. .virtualenv/bin/activate; FLASK_APP=main.py flask run

docker-build:
	docker build -t flask:develop .

docker-run:
	docker run -it -p 5000:80 flask:develop

docker-login:
	@$(eval login := $(shell (aws  --profile michalbagrowski ecr get-login --no-include-email --region $(REGION))))
	@${login}

version:
	docker build -t flask-$(REGION):$(VERSION) .
	docker tag flask-$(REGION):$(VERSION) $(AWS_ACCOUNT).dkr.ecr.$(REGION).amazonaws.com/flask-$(REGION):$(VERSION)
	docker push $(AWS_ACCOUNT).dkr.ecr.$(REGION).amazonaws.com/flask-$(REGION):$(VERSION)

bump:
	. .virtualenv/bin/activate; python scripts/bump.py

.PHONY: version


deploy-us-east-1:
	. .virtualenv/bin/activate; python scripts/deploy.py us-east-1
deploy-eu-west-1:
	. .virtualenv/bin/activate; python scripts/deploy.py eu-west-1
invalidate:
	. .virtualenv/bin/activate; python scripts/invalidate.py ${CLOUDFRONT_ID}

go: bump version invalidate
