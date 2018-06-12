provider "aws" {
    region  = "eu-central-1"
    shared_credentials_file  = "/aws/credentials"
    profile                  = "michalbagrowski"
}

data "terraform_remote_state" "ssl" {
    backend = "local"
    config {
        path = "${path.module}/../../ssl/terraform.tfstate"
    }
}

data "terraform_remote_state" "vpc" {
    backend = "local"
    config {
        path = "${path.module}/../../vpc/terraform.tfstate"
    }
}

resource "aws_api_gateway_domain_name" "domain" {
    domain_name = "per-elettronica.com"
    certificate_arn = "${data.terraform_remote_state.ssl.per-elettronica-com}"
}

resource "aws_api_gateway_base_path_mapping" "path" {
    api_id = "4gmslz6sma"
    stage_name = "prd"
    domain_name = "${aws_api_gateway_domain_name.domain.domain_name}"
}

output  "domain-name" {
    value="${aws_api_gateway_domain_name.domain.cloudfront_domain_name}"
}

output "zone-id" {
    value="${aws_api_gateway_domain_name.domain.cloudfront_zone_id}"
}