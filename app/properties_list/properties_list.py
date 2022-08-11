import requests

from flask import render_template, make_response, jsonify
from flask import current_app as app
from flask import Blueprint


api_prefix = app.config['PREFIX']
home = Blueprint(
    'event_profile', __name__,
    url_prefix=api_prefix
)

BASE_URL = app.config['BASE_URL']
EB_TOKEN = app.config['EB_TOKEN']


@home.route(f'/properties', methods=['GET'])
def all_properties():

    pagination, properties = get_next_page(f'{BASE_URL}/properties')
    next_page = pagination['next_page']

    return make_response(jsonify(properties), 200)


def get_next_page(next_page_url):
    res = requests.get(next_page_url, headers={
        'X-Authorization': EB_TOKEN})
    res = res.json()
    pagination = res['pagination']
    properties = res['content']

    return pagination, properties
