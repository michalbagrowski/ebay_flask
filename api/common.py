from jinja2 import Environment, FileSystemLoader,select_autoescape
import base64
import urllib
import operator
#from ebay_lib import func
#from ebaysdk.trading import Connection as Trading
from ebaysdk.finding import Connection as Finding
def get_env():
    return Environment(
            loader=FileSystemLoader( 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )

def get_template(template):
    env = get_env()
    return env.get_template(template)


def index(limit, cat, app_id, site_id, page, **kwargs):
    api = init_finding_api(app_id, site_id)
    callData = {
        "categoryId": cat,
        "outputSelector": ["GalleryInfo","PictureURLLarge"],
        "paginationInput": {
            "entriesPerPage": limit,
            "pageNumber": page
        }
    }

    items = api.execute('findItemsByCategory', callData)
    return items.dict()


def search(limit, rows, cat, query, app_id,site_id,title, description,queries, campagin_id, google_id, page = 1, **kwargs):
    page = int(page)

    items = get_search_items(query, cat, app_id,site_id, limit, page)

    keywords = []
    in_rows=  0

    if "searchResult" in items and "item" in items["searchResult"]:
        if limit == len(items["searchResult"]["item"]):
            in_rows = int(limit/rows)
        else:
            in_rows = int(len(items["searchResult"]["item"])/rows)

        keywords = get_keywords(items["searchResult"]["item"])
    return {
            "keywords": ", ".join(keywords),
            "title": title,
            "description": description,

            "items":  items,
            "pages": get_pages(page, int(items["paginationOutput"]["totalPages"])),
            "query": query,
            "queries": queries,
            "current_page": page,
            "campagin_id": campagin_id,
            "google_id": google_id,
            "total_pages": int(items["paginationOutput"]["totalPages"]),
            "limit": limit,
            "in_rows": in_rows
        }


def get_search_items(query, cat, app_id,site_id, limit = 10, page = 1):
    key_name = "search_"+ str(base64.b64encode(query.encode('ascii'))) + "_query_"+ str(cat) + "_" + str(limit) + "_" + str(page)
    api = init_finding_api(app_id, site_id)

    callData = {
        "categoryId": cat,
        "outputSelector": ["GalleryInfo","PictureURLLarge"],
        "paginationInput": {
            "entriesPerPage": limit,
            "pageNumber": page
        },
        "keywords": urllib.request.unquote(query)

    }

    items = api.execute('findItemsAdvanced', callData).dict()
    return items
def get_pages(page, total):
    pages = list(range(total))

    pages_first = pages[1:5];
    if page - 3 < 1:
        pages_current = pages[page:page+5]
    else:
        pages_current = pages[page-3:page+5]


    return list(set(pages_first+pages_current))

def get_keywords(items):
    keywords = []
    count_keys = {}
    for i in items:
        keywords = keywords + i["title"].split()

    for keyword in keywords:
        if keyword not in count_keys:
            count_keys[keyword] = 0
        count_keys[keyword] =count_keys[keyword] +1
    count_keys = sorted(count_keys.items(), key=operator.itemgetter(0))

    keywords = []

    for aaa in count_keys:
        if aaa[1] > 1:
            keywords.append(aaa[0])

    return keywords


def init_finding_api(app_id, site_id):

    find_api = Finding(
        domain = 'svcs.ebay.com',
        appid=app_id,
        config_file=None,
        siteid=site_id
    )

    return find_api
