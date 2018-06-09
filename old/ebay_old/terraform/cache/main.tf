provider "aws" {
    region  = "us-west-2"
    shared_credentials_file  = "/aws/credentials"
    profile                  = "michalbagrowski"
}

data "terraform_remote_state" "vpc" {
    backend = "local"
    config {
        path = "${path.module}/../vpc/terraform.tfstate"
    }
}

resource "aws_elasticache_subnet_group" "ebay-cache-subnet" {
    name = "ebay-cache"
    description = "ebay-cache"
    subnet_ids  = ["${data.terraform_remote_state.vpc.database_subnets}"]
}


resource "aws_elasticache_cluster" "lambda" {
    cluster_id           = "lambda"
    engine               = "memcached"
    node_type            = "cache.t2.micro"
    port                 = 11211
    num_cache_nodes      = 1
    parameter_group_name = "default.memcached1.4"
    security_group_ids = ["sg-2ff71052"]
    subnet_group_name = "ebay-cache"
}
