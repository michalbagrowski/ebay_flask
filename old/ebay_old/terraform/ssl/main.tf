provider "aws" {
    region  = "us-east-1"
    shared_credentials_file  = "/aws/credentials"
    profile                  = "michalbagrowski"
}

data "aws_acm_certificate" "hobby-drones-usa-com" {
        domain   = "hobby-drones-usa.com"
        statuses = ["ISSUED"]
}

data "aws_acm_certificate" "for-electronics-com" {
        domain   = "for-electronics.com"
        statuses = ["ISSUED"]
}

data "aws_acm_certificate" "per-elettronica-com" {
        domain   = "per-elettronica.com"
        statuses = ["ISSUED"]
}

data "aws_acm_certificate" "all-rc-parts-com" {
        domain   = "all-rc-parts.com"
        statuses = ["ISSUED"]
}

data "aws_acm_certificate" "fur-die-elektronik-de" {
        domain   = "fur-die-elektronik.de"
        statuses = ["ISSUED"]
}

output "hobby-drones-usa-com" {
    value = "${data.aws_acm_certificate.hobby-drones-usa-com.arn}"
}

output "per-elettronica-com" {
    value = "${data.aws_acm_certificate.per-elettronica-com.arn}"
}

output "for-electronics-com" {
    value = "${data.aws_acm_certificate.for-electronics-com.arn}"
}

output "fur-die-elektronik-de" {
    value = "${data.aws_acm_certificate.fur-die-elektronik-de.arn}"
}

output "all-rc-parts-com" {
    value = "${data.aws_acm_certificate.all-rc-parts-com.arn}"
}




#    name = "hobby-drones-usa.com."

#    name = "for-electronics.com."




#    name = "per-elettronica.com."
#}
