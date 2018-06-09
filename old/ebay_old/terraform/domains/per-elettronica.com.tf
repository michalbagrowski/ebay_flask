resource "aws_route53_record" "per-elettronica-com" {
    zone_id = "${aws_route53_zone.per-elettronica.id}"
    name = "per-elettronica.com."
    type= "A"
    alias {
        name = "${data.terraform_remote_state.per-elettronica-com.domain-name}"
        zone_id = "${data.terraform_remote_state.per-elettronica-com.zone-id}"
        evaluate_target_health = true
    }
}
