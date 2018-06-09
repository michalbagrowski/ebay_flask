REGION="us-west-2"
EBAY_LIB_VERSION=${shell cat requirements.txt | grep ebay_lib | awk -F "@" '{print $$3}'}
deploy:
	AWS_DEFAULT_PROFILE=michalbagrowski AWS_DEFAULT_REGION=${REGION} chalice deploy --stage prd

delete:
	AWS_DEFAULT_PROFILE=michalbagrowski AWS_DEFAULT_REGION=${REGION} chalice delete --stage prd

local:
	AWS_DEFAULT_PROFILE=michalbagrowski \
	AWS_DEFAULT_REGION=${REGION} \
	chalice local

nginx:
	sudo nginx -c /Users/acid/Projects/ebay/hobby-drones-usa.com/nginx.conf

update_ebay_lib:
	@rm -rf vendor/ebay_lib*
	@wget https://github.com/michalbagrowski/ebay_lib/archive/${EBAY_LIB_VERSION}.tar.gz
	@pip wheel ${EBAY_LIB_VERSION}.tar.gz
	@cp ebay_lib-${EBAY_LIB_VERSION}-py3-none-any.whl vendor/
	@cd vendor && unzip ebay_lib-${EBAY_LIB_VERSION}-py3-none-any.whl
	@rm ${EBAY_LIB_VERSION}.tar.gz
	@rm ebay_lib-${EBAY_LIB_VERSION}-py3-none-any.whl
	@rm vendor/ebay_lib-${EBAY_LIB_VERSION}-py3-none-any.whl
