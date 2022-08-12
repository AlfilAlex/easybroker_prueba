
import requests

from flask import render_template, make_response, request
from flask import current_app as app
from flask import Blueprint


api_prefix = app.config['PREFIX']
home = Blueprint(
    'home', __name__,
    url_prefix=api_prefix,
    template_folder='template',
    static_folder='static',
    static_url_path='home/static'
)

BASE_URL = app.config['BASE_URL']
EB_TOKEN = app.config['EB_TOKEN']
PAGE_LIMIT = 'limit=15'


@home.route(f'/properties', methods=['GET'])
def all_properties():

    page = request.args.get('page')
    PAGE = f'page={page}' if page else 'page=1'

    notfound = False
    try:
        pagination, properties = get_next_page(
            f'{BASE_URL}/properties?{PAGE_LIMIT}&{PAGE}')

    except requests.exceptions.HTTPError:
        notfound = True
        pagination = ''
        properties = ''

    return render_template('home.html', notfound=notfound,
                           pagination=pagination,
                           properties=properties)


def get_next_page(next_page_url):
    res = requests.get(next_page_url, headers={
        'X-Authorization': EB_TOKEN})

    if res.ok:
        res = res.json()
        properties = res['content']
        pagination = res['pagination']

        residue = pagination['total'] % pagination['limit']
        total_pages = int(pagination['total'] / pagination['limit'])
        pagination['total_pages'] = total_pages if not residue else total_pages + 1

        return pagination, properties

    else:
        raise res.raise_for_status()
