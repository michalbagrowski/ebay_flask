from chalice import Chalice, Response
from chalice import Chalice
from ebaysdk.trading import Connection as Trading
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection as Finding

app = Chalice(app_name='ebay')
app.debug = True
app_id = "MichaBag-ca6b-45b4-aab0-b1044c2fd03e"
dev_id = "c89fb856-8d3b-4e00-a1e0-8c2ad0306415"
cer_id = "8dd7a41c-1af8-41ee-aa42-08e3ed9a1cca"

token = "AgAAAA**AQAAAA**aAAAAA**MEOsWQ**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6ACloWjDpGKpwidj6x9nY+seQ**EN8BAA**AAMAAA**DJwe7KtHFcVp0TMSaV98mij/KT6FFJzxiLE9mzvhsIEeAL2YlDkMAoj6I23JbksbuNCuMLShdJd1Z6XfhYCgRH9/3iitf3zWIgrZnFWkVLsgrW80Ve0tCqbHX1uN2T5TnXmZ7/vYeITgwG9Qt31O/9/On6lod7JYBzWsBurgdWtNzuDsBHlwcPBfi7FI85fhrxsn7bknf2/0krTlS14nkXDfy1+2vjEivM+huf0rlXzOyT16Ow50VzZRNJcB4h0sxEXdai0L9RiHEVtGZdYNVpu41Lj0X61MzYcQck+RGptSy8fqYcGf39YZ6qVn/mYizWFshn6NIGTLF9F/700h8KwVCqWrk543NscxF38dmQDlZEt7mnMkfxrp6dWzniAMY14LzppDp9oZ+AMrWVZt9NfVN//wT7sIn8SSxHq/k2231Y9UqYipFxleTx8XpJts3y6IPYXkmslf6SYfOV/szuY6DkvB0ij7JrmFYSyZie3ItG29vrCmjBm1/T/4MBdcIPZwRD+Saeo0PjdIyNtnVKSP/EtdFJ/lm5IOp8WC6elL/dANaXXzPFRzBc+9MgrV9cJDjVmLTa48coqQDQq80hWxhX0HHA2h0Ky0poxeGEcu0Ytcrrjt3kyeFffh5ZVrtB08JBNfZN0yTJwRIiWsIJ0dZPL3dfzUEjawiX8Dco42gYGkZ9ETgQpR3P/6FHOJTw7O75XEzQPjwDgY5lBuRJXvMo0EiNvoxTZAlLPZFNlGY5FFLx4ySnWUn+Zzz0ZS"

@app.route('/')
def index():
    return Response(body="<html><title></title><body><h1>go go go</h1></body></html>", status_code=200, headers={'Content-Type':'text/html'})

@app.route('/robots.txt')
def robots():
    return Response(body="<html><title></title><body><h1>asd</h1><p>asd</p></body></html>", status_code=200, headers={'Content-Type':'text/html'})

@app.route('/favicon.ico')
def favicon():
    return Response(body="<html><title></title><body><h1>asd</h1><p>asd</p></body></html>", status_code=404, headers={'Content-Type':'text/html'})

@app.route("/category/{id}/{cat_name+}")
def category(id):
    from ebaysdk.finding import Connection as Finding
    from ebaysdk.exception import ConnectionError

    api = Finding(
        domain = 'svcs.ebay.com',
        appid=app_id,
        config_file=None,
        siteid="EBAY-US"
    )

    callData = {
        "categoryId": id,
        "outputSelector": ["GalleryInfo","PictureURLLarge"]
    }

    response = api.execute('findItemsByCategory', callData)
    print(response)
    data = "<html><head><script>window._epn = {campaign:5338177835};</script><script src=\"https://epnt.ebay.com/static/epn-smart-tools.js\"></script></head><body><ul>"
    for i in response.dict()["searchResult"]["item"]:
#{'itemId': '231505660468', 'title': 'Police Magnum mace pepper spray 1/2oz hot pink actuator self defense protection', 'globalId': 'EBAY-US', 'primaryCategory': {'categoryId': '79849', 'categoryName': 'Pepper Spray'}, 'galleryURL': 'http://thumbs1.ebaystatic.com/m/mYIVyE88preQeEP4Zxe1kNw/140.jpg', 'galleryInfoContainer': {'galleryURL': [{'_gallerySize': 'Large', 'value': 'http://thumbs1.ebaystatic.com/m/mYIVyE88preQeEP4Zxe1kNw/140.jpg'}, {'_gallerySize': 'Medium', 'value': 'http://thumbs1.ebaystatic.com/m/mYIVyE88preQeEP4Zxe1kNw/96.jpg'}, {'_gallerySize': 'Small', 'value': 'http://thumbs1.ebaystatic.com/m/mYIVyE88preQeEP4Zxe1kNw/80.jpg'}]}, 'viewItemURL': 'http://www.ebay.com/itm/Police-Magnum-mace-pepper-spray-1-2oz-hot-pink-actuator-self-defense-protection-/231505660468', 'paymentMethod': 'PayPal', 'autoPay': 'false', 'postalCode': '32829', 'location': 'Orlando,FL,USA', 'country': 'US', 'shippingInfo': {'shippingServiceCost': {'_currencyId': 'USD', 'value': '0.0'}, 'shippingType': 'Free', 'shipToLocations': 'Worldwide', 'expeditedShipping': 'false', 'oneDayShippingAvailable': 'false', 'handlingTime': '1'}, 'sellingStatus': {'currentPrice': {'_currencyId': 'USD', 'value': '4.99'}, 'convertedCurrentPrice': {'_currencyId': 'USD', 'value': '4.99'}, 'sellingState': 'Active', 'timeLeft': 'P25DT10H17M37S'}, 'listingInfo': {'bestOfferEnabled': 'false', 'buyItNowAvailable': 'false', 'startTime': '2015-03-15T00:21:19.000Z', 'endTime': '2017-09-30T00:21:19.000Z', 'listingType': 'StoreInventory', 'gift': 'false', 'watchCount': '118'}, 'returnsAccepted': 'true', 'condition': {'conditionId': '1000', 'conditionDisplayName': 'New'}, 'isMultiVariationListing': 'false', 'pictureURLLarge': 'http://i.ebayimg.com/00/s/MTUxMlgxMDc5/z/DpsAAOSwU-pXs2n1/$_1.JPG', 'topRatedListing': 'true'}
        print(i)
        if "pictureURLLarge" in i:
            data+='<li><a href="'+i["viewItemURL"]+'">'+i['title']+'<img src="'+i["pictureURLLarge"]+'" /></a></ul>'
    data += "</ul></body></html>"

    return Response(body=data, status_code=404, headers={'Content-Type':'text/html'})

@app.route('/test')
def test():
    api = get_tranding_api()

    callData = {
        'DetailLevel': 'ReturnAll',
        'LevelLimit':  1
    }

    response = api.execute('GetCategories', callData)
    print(response.dict())
    data = "<ul>"
    for i in response.dict()["CategoryArray"]["Category"]:
        if i['CategoryParentID'] == i['CategoryID']:
            print(i)
            data += "<li><a href=\"/category/"+i["CategoryID"]+"/"+i["CategoryName"]+"\">"+i["CategoryName"]+"</a></li>"
    data += "<ul>"
    return Response(body=data, status_code=200, headers={'Content-Type':'text/html'})

#def

def get_tranding_api(site_id = 0):
    return Trading(
        domain='api.ebay.com',
        appid=app_id,
        devid=dev_id,
        certid=cer_id,
        token=token,
        config_file=None,
        siteid=str(site_id))

import boto3
import json
import os
def get_all_categories(site_id = "0"):
    temp = "/tmp/categories_"+site_id
    if os.path.isfile(temp):
        with(open(temp)) as data_file:
            categories = json.load(data_file)
    else:

        api = get_tranding_api();
        callData = {
            'DetailLevel': 'ReturnAll'
        }
        response = api.execute('GetCategories', callData)


        categories = response.dict()["CategoryArray"]["Category"]
        f = open (temp, "w")
        f.write(json.dumps(response.dict()["CategoryArray"]["Category"]))

    items = []
    i=0
    length = len(categories)
    for cat in categories:

        cat["SiteId"] = "0";
        if i < 20:
            items.append(cat)
            i = i + 1
        else:

            items.append(cat)
            save(items)
            i = 0
            items = []
    save(items)

def save(items):

    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ebay_categories')
#    for i in items:
#        table.put_item(Item=i)
    with table.batch_writer(overwrite_by_pkeys=['CategoryID']) as batch:
        for i in items:
            if i["CategoryID"] == i["CategoryParentID"]:
                i["Root"] = "true"
            else:
                i["Root"] = "false"
            batch.put_item(Item=i)

sites = ["0","2","3","15","16","23","71","77","100","101","123","146","186","193","201","203","205","207","210","211","212","216"]
for site in sites:
    get_all_categories(site)
from boto3.dynamodb.conditions import Key, Attr

def search():
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ebay_categories')
    response = table.query(
        IndexName="Root-index",
        KeyConditionExpression=Key("Root").eq("true")
    )
    items = response['Items']
    print(items)

def search_cat(cat_id):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ebay_categories')
    response = table.query(
        IndexName="CategoryParentID-index",
        KeyConditionExpression=Key("CategoryParentID").eq(cat_id)
    )
    items = response['Items']
    print(items)

#search_cat("11116")
# The view function above will return {"hello": "world"}
# whenever you mae an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
