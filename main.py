from flask import Flask
from api import common
app = Flask(__name__)

@app.route("/")
def hello():
    template = common.get_template('index.html')
    index = common.index()
    rows = 3
    limit = 51

    for i in index:
        print(i)
    a = {
        "current_page": 0,
        "total_pages": 0,
        "items": index,
        "in_rows": int(limit/rows)+1
    }

    response = {
        "statusCode": 200,
        "body": template.render(**a),
        "headers": {
            "Content-Type": "text/html"
        }
    }

    return template.render(**a)
