resource "aws_dynamodb_table" "ebay_categories" {
    name = "ebay_categories"
    read_capacity = 5
    write_capacity = 20

    hash_key = "CategoryID"

    attribute {
        name = "CategoryID"
        type = "S"
    }

    attribute {
        name = "CategoryParentID"
        type = "S"
    }

    attribute {
        name = "Root"
        type = "S"
    }

    global_secondary_index {
        name = "CategoryParentID-index"
        hash_key = "CategoryParentID"
        projection_type = "ALL"
        read_capacity =  "5"
        write_capacity = "20"
    }

    global_secondary_index {
        name = "Root-index"
        hash_key = "Root"
        projection_type = "ALL"
        read_capacity =  "5"
        write_capacity = "20"
    }

}
