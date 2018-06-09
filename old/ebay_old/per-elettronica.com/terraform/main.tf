provider "aws" {
    region  = "eu-central-1"
    shared_credentials_file  = "/aws/credentials"
    profile                  = "michalbagrowski"
}

data "terraform_remote_state" "ssl" {
    backend = "local"

    config {
        path = "${path.module}/../../terraform/ssl/terraform.tfstate"
    }
}

resource "aws_api_gateway_domain_name" "api_domain" {
    domain_name = "${var.api_domain}"
    certificate_arn = "${data.terraform_remote_state.ssl.per-elettronica-com}"
}
