import json
from api import common

def asd(event, context):
    response = {
        "statusCode": 200,
        "body": "asdaa"
    }
    return response

def index(event, context):
    template = common.get_template('index.html')
    index = common.index()
    a = {
        "current_page": 0,
        "total_pages": 0,
        "items": {
            "searchResult": []
        },
    }

    response = {
        "statusCode": 200,
        "body": template.render(**a),
        "headers": {
            "Content-Type": "text/html"
        }
    }

    return response
