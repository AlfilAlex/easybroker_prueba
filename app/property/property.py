import requests

from flask import render_template, request, make_response
from flask import current_app as app
from flask import Blueprint


api_prefix = app.config['PREFIX']
property_profile = Blueprint(
    'property_profile', __name__,
    url_prefix=api_prefix,
    template_folder='template',
    static_folder='static'
)

BASE_URL = app.config['BASE_URL']
EB_TOKEN = app.config['EB_TOKEN']


# @cross_origin(supports_credentials=True, origins=['*'], allow_headers=['Content-Type', 'Authorization'])
@property_profile.route(f'/properties/<property_id>', methods=['GET'])
def property_page(property_id):
    res = requests.get(f'{BASE_URL}/properties/{property_id}', headers={
        'X-Authorization': EB_TOKEN})
    property_info = res.json()
    # print(property_info)

    return render_template('property.html', property_info=property_info)


@property_profile.route(f'/properties/<property_id>', methods=['POST'])
def property_contact(property_id):
    form_data = request.form.to_dict()
    form_data['property_id'] = property_id
    form_data['source'] = 'cabimax.com'

    res = requests.post(f'{BASE_URL}/contact_requests', json=form_data, headers={
        'X-Authorization': EB_TOKEN,
        "accept": "application/json",
        'content-type': 'application/json'})

    if res.ok:
        return render_template('succesfull_contact.html')
    else:
        make_response({'error': res.json()}, 400)
