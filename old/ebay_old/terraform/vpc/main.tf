provider "aws" {
    region  = "us-west-2"
    shared_credentials_file  = "/aws/credentials"
    profile                  = "michalbagrowski"
}

resource "aws_vpc" "main" {
    cidr_block = "10.0.0.0/16"
    tags {
        Name = "Ebay VPC"
    }
}

resource "aws_internet_gateway" "ig" {
    vpc_id = "${aws_vpc.main.id}"
}

resource "aws_subnet" "public" {
    count = 3
    vpc_id = "${aws_vpc.main.id}"

    cidr_block = "${element(split(",", var.public_subnets), count.index)}"
    availability_zone = "${element(split(",", var.availability_zones), count.index % length(compact(split(",", var.availability_zones))))}"
    tags {
        Name = "public-ebay-${element(split(",", var.availability_zones), count.index % length(compact(split(",", var.availability_zones))))}"
    }
}

resource "aws_subnet" "private" {
    count = 3
    vpc_id = "${aws_vpc.main.id}"

    cidr_block = "${element(split(",", var.private_subnets), count.index)}"
    availability_zone = "${element(split(",", var.availability_zones), count.index % length(compact(split(",", var.availability_zones))))}"
    tags {
        Name = "private-ebay-${element(split(",", var.availability_zones), count.index % length(compact(split(",", var.availability_zones))))}"
    }
}

resource "aws_subnet" "database" {
    count = 3
    vpc_id = "${aws_vpc.main.id}"

    cidr_block = "${element(split(",", var.database_subnets), count.index)}"
    availability_zone = "${element(split(",", var.availability_zones), count.index % length(compact(split(",", var.availability_zones))))}"
    tags {
        Name = "database-ebay-${element(split(",", var.availability_zones), count.index % length(compact(split(",", var.availability_zones))))}"
        Tier = "Database"
    }
}

resource "aws_route_table" "private_nat" {

    vpc_id = "${aws_vpc.main.id}"
    tags {
        Name = "private_nat"
    }
}

resource "aws_route_table" "public_igw" {
    vpc_id = "${aws_vpc.main.id}"
    tags {
        Name = "public_igw"
    }
}

resource "aws_route" "private_nat" {
    route_table_id = "${aws_route_table.private_nat.id}"
    destination_cidr_block= "0.0.0.0/0"
    nat_gateway_id = "${aws_nat_gateway.natgtw.id}"

}

resource "aws_route" "public_igw" {
    route_table_id = "${aws_route_table.public_igw.id}"
    destination_cidr_block = "0.0.0.0/0"
    gateway_id = "${aws_internet_gateway.ig.id}"
}


resource "aws_route_table_association" "database" {
    count = "${length(compact(split(",", var.database_subnets)))}"
    subnet_id = "${element(aws_subnet.private.*.id, count.index)}"
    route_table_id = "${aws_route_table.private_nat.id}"
}


resource "aws_route_table_association" "private" {
    count = "${length(compact(split(",", var.private_subnets)))}"
    subnet_id = "${element(aws_subnet.private.*.id, count.index)}"
    route_table_id = "${aws_route_table.private_nat.id}"
}

resource "aws_route_table_association" "public" {
    count = "${length(compact(split(",", var.public_subnets)))}"
    subnet_id = "${element(aws_subnet.public.*.id, count.index)}"
    route_table_id = "${aws_route_table.public_igw.id}"
}


resource "aws_eip" "nat"  {
    vpc = true
}

resource "aws_nat_gateway" "natgtw" {
    allocation_id = "${aws_eip.nat.id}"
    subnet_id = "${aws_subnet.public.0.id}"
}


data "aws_subnet_ids" "database_subnets" {
    vpc_id = "${aws_vpc.main.id}"
    tags {
        Tier = "Database"
    }
}

output "database_subnets" {
    value="${data.aws_subnet_ids.database_subnets.ids}"
}
