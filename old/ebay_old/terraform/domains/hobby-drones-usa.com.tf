resource "aws_route53_record" "hobby-drones-usa-com" {
    zone_id = "${aws_route53_zone.hobby-drones-usa.id}"
    name = "hobby-drones-usa.com."
    type= "A"
    alias {
        name = "${data.terraform_remote_state.hobby-drones-usa-com.domain-name}"
        zone_id = "${data.terraform_remote_state.hobby-drones-usa-com.zone-id}"
        evaluate_target_health = false
    }

}
