provider "aws" {
    region  = "us-west-2"
    shared_credentials_file  = "/aws/credentials"
    profile                  = "michalbagrowski"
}

data "terraform_remote_state" "fur-die-elektronik-de" {
    backend = "local"
    config {
        path = "${path.module}/../apis/fur-die-elektronik.de/terraform.tfstate"
    }
}

data "terraform_remote_state" "per-elettronica-com" {
    backend = "local"
    config {
        path = "${path.module}/../apis/per-elettronica.com/terraform.tfstate"
    }
}

data "terraform_remote_state" "for-electronics-com" {
    backend = "local"
    config {
        path = "${path.module}/../apis/for-electronics.com/terraform.tfstate"
    }
}

data "terraform_remote_state" "hobby-drones-usa-com" {
    backend = "local"
    config {
        path = "${path.module}/../apis/hobby-drones-usa.com/terraform.tfstate"
    }
}



data "terraform_remote_state" "all-rc-parts-com" {
    backend = "local"
    config {
        path = "${path.module}/../apis/all-rc-parts.com/terraform.tfstate"
    }
}

resource "aws_route53_zone" "hobby-drones-usa" {
    name = "hobby-drones-usa.com."
    comment = "HostedZone created by Route53 Registrar"
    force_destroy = false
}

resource "aws_route53_zone" "for-electronics" {
    name = "for-electronics.com."
    comment = "HostedZone created by Route53 Registrar"
    force_destroy = false
}

resource "aws_route53_zone" "per-elettronica" {
    name = "per-elettronica.com."
    comment = "HostedZone created by Route53 Registrar"
    force_destroy = false
}

resource "aws_route53_zone" "fur-die-elektronik" {
    name = "fur-die-elektronik.de."
    comment = "HostedZone created by Route53 Registrar"
    force_destroy = false
}

resource "aws_route53_zone" "all-rc-parts" {
    name = "all-rc-parts.com."
    comment = "HostedZone created by Route53 Registrar"
    force_destroy = false

}
