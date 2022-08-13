import requests

from flask import render_template, request, make_response
from flask import current_app as app
from flask import Blueprint


api_prefix = app.config['PREFIX']
property_profile = Blueprint(
    'property_profile', __name__,
    url_prefix=api_prefix,
    template_folder='template',
    static_folder='static',
    static_url_path='property/static'
)

EB_BASE_URL = app.config['EB_BASE_URL']
EB_TOKEN = app.config['EB_TOKEN']


@property_profile.route(f'/properties/<property_id>', methods=['GET'])
def property_profile_page(property_id):
    res = requests.get(f'{EB_BASE_URL}/properties/{property_id}', headers={
        'X-Authorization': EB_TOKEN})
    property_info = res.json()
    return render_template('property.html', property_info=property_info)


@property_profile.route(f'/properties/<property_id>', methods=['POST'])
def property_contact(property_id):
    contact_form_data = request.form.to_dict()
    contact_form_data['property_id'] = property_id
    contact_form_data['source'] = 'cabimax.com'  # Fictisious domain origin

    res = requests.post(f'{EB_BASE_URL}/contact_requests', json=contact_form_data, headers={
        'X-Authorization': EB_TOKEN,
        "accept": "application/json",
        'content-type': 'application/json'})

    if res.ok:
        return render_template('contact_res.html', data=contact_form_data)
    else:
        return make_response({'error': res.json()}, res.status_code)
