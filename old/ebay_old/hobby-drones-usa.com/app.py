from chalice import Chalice, Response
from chalice import Chalice
import chalicelib
from chalicelib import config
from ebay_lib import func
from ebay_lib import static
from jinja2 import Environment, PackageLoader, select_autoescape

app = Chalice(app_name='hobby-drones-usa-com')
app.debug = True

def get_template(template):
    env = get_env()
    return env.get_template(template)

def get_env():
    return Environment(
            loader=PackageLoader('chalicelib', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )

@app.route('/')
def index():
    template = get_template('index.html')
    kwargs = func.index()
    return Response(
        body = template.render(**kwargs),
        status_code = 200,
        headers = {
            "Content-Type": "text/html"
        }
    )

@app.route('/search/{query}/{page}')
def search(query, page = 1):
    return func.search(query, page)

@app.route('/category/{category}/{page}')
def category(category, page = 1):
    return func.category(category, page)

@app.route('/main.css')
def main_css():
    return static.main_css();

@app.route('/reset.css')
def reset_css():
    return static.reset_css();

@app.route('/sitemap.xml')
def sitemap():
    return static.sitemap()


@app.route('/favicon.ico')
def favicon():
    return static.favicon()

def get_categories(cats):
    result  = []
    for cat in cats:
        dynamodb = get_dynamodb()
        table = dynamodb.Table('ebay_categories')
        response = table.query(
            IndexName="CategoryParentID-index",
            KeyConditionExpression=Key("CategoryParentID").eq(cat)
        )
        items = response['Items']
        result += items
    return result

def get_dynamodb():
    return boto3.resource('dynamodb')
