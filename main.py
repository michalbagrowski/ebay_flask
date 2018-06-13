from flask import Flask
from flask import request
from api import common
from functools import wraps
from flask import Flask, make_response
from flask import Response
import os

app = Flask(__name__)
default = "hobby-drones-usa.com"
#default = "all-rc-parts.com"
#default = "fur-die-elektronik.de"

config = {
    "fur-die-elektronik.de": {
        "limit": 66,
        "rows": 3,
        "cat": 92074,
        "google_id": "UA-120816592-1",
        "campagin_id": "5338325667",
        "app_id":  "MichaBag-ca6b-45b4-aab0-b1044c2fd03e",
        "title": "-",
        "description": "-",
        "queries": [
            "TV"
        ],
        "domain": "fur-die-elektronik.de",
        "site_id": "EBAY-DE"
    },
    "hobby-drones-usa.com" : {
        "limit": 66,
        "rows": 3,
        "cat": 179697,
        "google_id": "UA-106144387-1",
        "campagin_id": "5338177835",
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
        "domain": "hobby-drones-usa.com",
        "site_id": "EBAY-US"
    },

    "all-rc-parts.com" : {
        "limit": 66,
        "rows": 3,
        "cat": 2562,
        "google_id": "UA-120723509-1",
        "campagin_id": "5338182915",
        "app_id":  "MichaBag-ca6b-45b4-aab0-b1044c2fd03e",
        "title": "RC Parts",
        "description": "RC Parts",
        "queries": [
            "HPI",
            "HSP",
            "Maverics Strada",
            "Traxxas"
        ],
        "domain": "all-rc-parts.com",
        "site_id": "EBAY-US"
    }
}


def get_config(headers):
    global config, default
    if headers["host"] in config:
        return config[headers["host"]]
    else:
        return config[default]

def init(headers, template):
    return (get_config(headers), common.get_template(template))

@app.route("/")
def index():
    (config, template) = init(request.headers, "index.html")

    config["page"] = 1

    page_data = common.call(common.index, config)
    return template.render(**page_data)

@app.route("/search/<query>/<page>")
def search(query, page):
    (config, template) = init(request.headers, "index.html")

    config["page"] = page
    config["query"] = query

    page_data = common.call(common.search, config)
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

@app.route("/google3830beaa9b83b405.html")
def google_1():
    return "google-site-verification: google3830beaa9b83b405.html"

@app.route("/google25ec626b770b47f2.html")
def google_2():
    return "google-site-verification: google25ec626b770b47f2.html"

@app.route("/ping")
def ping():
    return "ping"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
