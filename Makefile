NAME="flask"
VERSION=`cat VERSION`
#REGION="us-east-1"
AWS_ACCOUNT="206636293913"
CLOUDFRONT_ID="E3V1JSQA1HZG36"
run:
	. .virtualenv/bin/activate; FLASK_APP=main.py flask run

docker-build:
	docker build -t flask:develop .

docker-run:
	docker run -it -p 5000:80 flask:develop


docker-login: docker-login-us-east-1 docker-login-eu-west-1

docker-login-us-east-1:
	@$(eval login := $(shell (aws  --profile michalbagrowski ecr get-login --no-include-email --region us-east-1)))
	@${login}

docker-login-eu-west-1:
	@$(eval login := $(shell (aws  --profile michalbagrowski ecr get-login --no-include-email --region us-east-1)))
	@${login}

version: version-us-east-1 version-eu-west-1

version-us-east-1:
	docker build -t flask-us-east-1:$(VERSION) .
	docker tag flask-us-east-1:$(VERSION) $(AWS_ACCOUNT).dkr.ecr.us-east-1.amazonaws.com/flask-us-east-1:$(VERSION)
	docker push $(AWS_ACCOUNT).dkr.ecr.us-east-1.amazonaws.com/flask-us-east-1:$(VERSION)

version-eu-west-1:
	docker build -t flask-eu-west-1:$(VERSION) .
	docker tag flask-eu-west-1:$(VERSION) $(AWS_ACCOUNT).dkr.ecr.eu-west-1.amazonaws.com/flask-eu-west-1:$(VERSION)
	docker push $(AWS_ACCOUNT).dkr.ecr.eu-west-1.amazonaws.com/flask-eu-west-1:$(VERSION)

bump:
	. .virtualenv/bin/activate; python scripts/bump.py

.PHONY: version

deploy: deploy-us-east-1 deploy-eu-west-1

deploy-us-east-1:
	. .virtualenv/bin/activate; python scripts/deploy.py us-east-1
deploy-eu-west-1:
	. .virtualenv/bin/activate; python scripts/deploy.py eu-west-1

invalidate:
	. .virtualenv/bin/activate; python scripts/invalidate.py ${CLOUDFRONT_ID}

go: bump version invalidate
