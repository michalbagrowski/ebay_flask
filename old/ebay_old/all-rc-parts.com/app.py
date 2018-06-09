from chalice import Chalice, Response
from ebay_lib import func
from chalicelib import config
from ebay_lib import func
from jinja2 import Environment, PackageLoader, select_autoescape

app = Chalice(app_name='all-rc-parts-com')
app.debug = True


def get_template(name):
    env = get_env()
    return env.get_template(name)

def get_env():
    return Environment(
            loader=PackageLoader('chalicelib', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )

@app.route('/')
def index():
    template = get_template('index.html')
    kwargs = func.index()
    kwargs["searches"] = config.searches
    kwargs["campagin"] = config.campagin
    return Response(
        body = template.render(**kwargs),
        status_code = 200,
        headers = {
            "Content-Type": "text/html"
        }
    )

@app.route('/search/{query}/{page}')
def search(query, page = 1):
    template = get_template('index.html')
    kwargs = func.search(query, page)
    kwargs["searches"] = config.searches
    kwargs["campagin"] = config.campagin
    return Response(
        body = template.render(**kwargs),
        status_code = 200,
        headers = {
            "Content-Type": "text/html"
        }
    )

@app.route('/category/{category}/{page}')
def category(category, page = 1):
    template = get_template('index.html')
    kwargs = func.category(category, page)
    kwargs["searches"] = config.searches
    kwargs["campagin"] = config.campagin
    return Response(
        body = template.render(**kwargs),
        status_code = 200,
        headers = {
            "Content-Type": "text/html"
        }
    )

@app.route('/sitemap.xml')
def sitemap():
    template = get_template('sitemap.xml')
    return Response(
        body = template.render(
            queries =  ["HPS maverics","Traxxas","Maveric Strada"]
        ),
        status_code = 200,
        headers = {
            "Content-Type": "text/html"
        }
    )

@app.route('/main.css')
def main_css():
    template = get_template('main.css')
    return Response(
        body = template.render(
        ),
        status_code = 200,
        headers = {
            "Content-Type": "text/css"
        }
    )

@app.route('/reset.css')
def reset_css():
    template = get_template('reset.css')
    return Response(
        body = template.render(
        ),
        status_code = 200,
        headers = {
            "Content-Type": "text/css"
        }
    )

@app.route('/favicon.ico')
def favicon():
    return Response(body="no", status_code=404, headers={'Content-Type':'text/html'})
