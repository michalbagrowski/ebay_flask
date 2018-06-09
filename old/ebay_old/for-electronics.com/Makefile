REGION="us-west-2"

deploy:
	AWS_DEFAULT_PROFILE=michalbagrowski AWS_DEFAULT_REGION=${REGION} chalice deploy --stage prd

delete:
	AWS_DEFAULT_PROFILE=michalbagrowski AWS_DEFAULT_REGION=${REGION} chalice delete --stage prd

local-drones:
	AWS_DEFAULT_PROFILE=michalbagrowski \
	AWS_DEFAULT_REGION=${REGION} \
	chalice local

nginx:
	sudo nginx -c /Users/acid/Projects/ebay/ebay_api/nginx.conf
