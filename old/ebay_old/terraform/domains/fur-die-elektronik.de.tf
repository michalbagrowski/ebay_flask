resource "aws_route53_record" "fur-die-elektronik-de" {
    zone_id = "${aws_route53_zone.fur-die-elektronik.id}"
    name = "fur-die-elektronik.de."
    type= "A"
    alias {
        name = "${data.terraform_remote_state.fur-die-elektronik-de.domain-name}"
        zone_id = "${data.terraform_remote_state.fur-die-elektronik-de.zone-id}"
        evaluate_target_health = true
    }
}
