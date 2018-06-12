from flask import Flask
from flask import request
from api import common
from functools import wraps
from flask import Flask, make_response
from flask import Response

app = Flask(__name__)
config = {
    "localhost:5000" : {
        "limit": 66,
        "rows": 3,
        "cat": 179697,
        "app_id":  "MichaBag-ca6b-45b4-aab0-b1044c2fd03e",
        "title": "DRONY DJI, MAVIC, SPARK, PARROT",
        "description": "All frones for you",
        "queries": [
            "Drones",
            "Battery",
            "Propeller",
            "DJI Mavic Pro",
            "DJI Spark",
            "Syma",
            "Parrot",
            "3d Robotocis",
            "GoPro",
            "Husban"
        ],
        "domain": "hobby-drones-usa.com"

    }
}


def get_config(headers):
    global config
    if headers["host"] in config:
        return config[headers["host"]]
    else:
        return config["localhost:5000"]

def init(headers, template):
    return (get_config(headers), common.get_template(template))

@app.route("/")
def hello():
    (config, template) = init(request.headers, "index.html")

    page_data = {
        "current_page": 0,
        "total_pages": 0,
        "items": common.index(config["limit"], config["cat"], config["app_id"],page=1),
        "in_rows": int(config["limit"]/config["rows"]),
        "queries": config["queries"]
    }

    return template.render(**page_data)


@app.route("/search/<query>/<page>")
def search(query, page):
    (config, template) = init(request.headers, "index.html")
    config["page"] = page
    config["query"] = query
    page_data=  common.search(**config)
    return template.render(**page_data)

@app.route("/sitemap.xml")
def sitemap():
    (config, template) = init(request.headers, "sitemap.xml")

    resp = Response(template.render(**config))
    resp.headers['Content-Type'] = 'text/xml'
    return resp


@app.route("/main.css")
def css_main():
    template = common.get_template('main.css')
    resp = Response(template.render({}))
    resp.headers['Content-Type'] = 'text/css'
    return resp

@app.route("/reset.css")
def css_reset():
    template = common.get_template('reset.css')
    resp = Response(template.render({}))
    resp.headers['Content-Type'] = 'text/css'
    return resp
