import requests

from flask import render_template, make_response, request
from flask import current_app as app
from flask import Blueprint


api_prefix = app.config['PREFIX']
home = Blueprint(
    'home', __name__,
    url_prefix=api_prefix,
    template_folder='template'
)

BASE_URL = app.config['BASE_URL']
EB_TOKEN = app.config['EB_TOKEN']
PAGE_LIMIT = 'limit=5'


@home.route(f'/properties', methods=['GET'])
def all_properties():

    page = request.args.get('page')
    if page:
        PAGE = f'page={page}'
    else:
        PAGE = 'page=1'

    pagination, properties = get_next_page(
        f'{BASE_URL}/properties?{PAGE_LIMIT}&{PAGE}')

    return render_template('home.html', pagination=pagination,
                           properties=properties)


def get_next_page(next_page_url):
    res = requests.get(next_page_url, headers={
        'X-Authorization': EB_TOKEN})
    res = res.json()
    pagination = res['pagination']
    properties = res['content']

    return pagination, properties
