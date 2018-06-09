resource "aws_route53_record" "for-electronics-com" {
    zone_id = "${aws_route53_zone.for-electronics.id}"
    name = "for-electronics.com."
    type= "A"
    alias {
        name = "${data.terraform_remote_state.for-electronics-com.domain-name}"
        zone_id = "${data.terraform_remote_state.for-electronics-com.zone-id}"
        evaluate_target_health = true
    }
}
