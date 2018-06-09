resource "aws_route53_record" "all-rc-parts-com" {
    zone_id = "${aws_route53_zone.all-rc-parts.id}"
    name = "all-rc-parts.com."
    type= "A"
    alias {
        name = "${data.terraform_remote_state.all-rc-parts-com.domain-name}"
        zone_id = "${data.terraform_remote_state.all-rc-parts-com.zone-id}"
        evaluate_target_health = true
    }
}
