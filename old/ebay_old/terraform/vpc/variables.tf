variable "public_subnets" {
    default = "10.0.0.0/23,10.0.2.0/23,10.0.4.0/23"
}
variable "private_subnets" {
    default = "10.0.6.0/23,10.0.8.0/23,10.0.10.0/23"
}
variable "database_subnets" {
    default = "10.0.12.0/23,10.0.14.0/23,10.0.16.0/23"
}
variable "availability_zones" {
    default = "us-west-2a,us-west-2b,us-west-2c"
}
