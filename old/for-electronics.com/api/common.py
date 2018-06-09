from jinja2 import Environment, FileSystemLoader,select_autoescape
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


def index():
    cats = ["179697", "182969"]
    limit = 100
    page = 1
#    items = get_items(config.cats[0], limit)
    api = init_finding_api()
    cat = cats[0]
    callData = {
        "categoryId": cat,
        "outputSelector": ["GalleryInfo","PictureURLLarge"],
        "paginationInput": {
            "entriesPerPage": limit,
            "pageNumber": page
        }
    }
    print|(callData)
    return items = api.execute('findItemsByCategory', callData).dict()

def init_finding_api():
    app_id = "MichaBag-ca6b-45b4-aab0-b1044c2fd03e"
    find_api = Finding(
        domain = 'svcs.ebay.com',
        appid=app_id,
        config_file=None,
        siteid="EBAY-US"
    )

    return find_api
