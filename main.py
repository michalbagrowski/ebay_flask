from flask import Flask
from flask import request
from api import common
from functools import wraps
from flask import Flask, make_response
from flask import Response
from flask import g
import os

app = Flask(__name__)
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
def init(headers, template):
    #default = "hobby-drones-usa.com"
    #default = "all-rc-parts.com"
    #default = "fur-die-elektronik.de"
    default = "for-electronics.com"
    #default = "per-elettronica.com"

    config = {
        "default": {
            "categories_enabled": False,
            "limit": 66,
            "rows": 3,
            "app_id":  "MichaBag-ca6b-45b4-aab0-b1044c2fd03e",
            "main_name": "placeholder",
            "queries": [],
            "title": "-",
            "description": "-",
        },
        "a:5000":{
            "categories_enabled": True,
            "cat": 12576,
            "campagin_id":"5338326020",
            "site_id": "EBAY-IT",
            "domain": "per-elettronica.com",
            "google_id": "UA-120797026-1"
        },
        "for-electronics.com":{
            "cat": 293,
            "site_id": "EBAY-US",
            "campagin_id": "5338326021",
            "categories_enabled": True,
            "doman": "for-electronics.com",
            "google_id": "UA-120798797-1"
        },
        "fur-die-elektronik.de": {
            "cat": 92074,
            "google_id": "UA-120816592-1",
            "campagin_id": "5338325667",
            "domain": "fur-die-elektronik.de",
            "site_id": "EBAY-DE",
            "categories_enabled": True,
            "main_name": "elektronik"
        },
        "b:5000" : {
            "cat": 179697,
            "google_id": "UA-106144387-1",
            "campagin_id": "5338177835",
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
            "site_id": "EBAY-US",
            "main_name": "drone"
        },
        "all-rc-parts.com" : {
            "google_id": "UA-120723509-1",
            "cat": 2562,
            "campagin_id": "5338182915",
            "title": "RC Parts",
            "description": "RC Parts",
            "queries": [
                "HPI",
                "HSP",
                "Maverics Strada",
                "Traxxas"
            ],
            "domain": "all-rc-parts.com",
            "site_id": "EBAY-US",
            "main_name": "parts"
        }
    }
    return (get_config(config, default, headers), common.get_template(template))

def fill_default(default, configuration):
    default.update(configuration)
    return default

def get_config(config, default, headers):
    if headers["host"] in config:
        return fill_default(config["default"], config[headers["host"]])
    else:
        return fill_default(config["default"], config[default])


@app.route("/")
def index():
    (config, template) = init(request.headers, "index.html")
    config["page"] = 1
    config["category"] = str(config["cat"])+"/"+config["main_name"]
    page_data = common.call(common.index, config)

    return template.render(**page_data)

@app.route("/search/<query>/<page>")
def search(query, page):
    (config, template) = init(request.headers, "index.html")

    config["page"] = page
    config["query"] = query

    page_data = common.call(common.search, config)

    return template.render(**page_data)

@app.route("/category/<cat_id>/<name>/<page>")
def category(cat_id, name, page):
    (config, template) = init(request.headers, "index.html")


    config["cat"] = cat_id
    config["page"] = page

    page_data = common.call(common.index, config)
    up = {
        "category": cat_id+"/" +name
    }
    page_data.update(up)
    return template.render(**page_data)

@app.route("/sitemap.xml")
def sitemap():
    (config, template) = init(request.headers, "sitemap.xml")

    up ={
        "categories": common.getCategories(
            config["categories_enabled"], config["site_id"], config["cat"]
            )
    }

    config.update(up)

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

@app.route("/google62d0c1e2b6b1a5ea.html")
def google_3():
    return "google-site-verification: google62d0c1e2b6b1a5ea.html"

@app.route("/google62d0c1e2b6b1a5ea.html")
def google_4():
    return "google-site-verification: google62d0c1e2b6b1a5ea.html"

@app.route("/ping")
def ping():
    return "ping"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
