import pytest
import json

from app import create_app
from requests import Response

TEST_PROPERTY = {'public_id': 'EB-XXXXX', 'title': 'Departamento Fonda de Eduviges',
                 'description': 'Casa de varios cuartos sin iluminación y con almas perdidas',
                 'location': {'name': 'Del Valle Oriente, San Pedro Garza García, Nuevo León', 'latitude': 0.0, 'longitude': 0.0},
                 'property_type': 'Departamento', 'created_at': '2021-01-29T18:57:04-06:00',
                 'updated_at': '2022-08-07T14:25:35-05:00', 'published_at': '2022-08-07T14:25:35-05:00',
                 'operations': [{'type': 'rental', 'amount': 48000.0, 'currency': 'MXN', 'formatted_amount': '$48,000', 'commission': {'type': 'percentage'}, 'unit': 'total'}],
                 'property_images': [{'title': None, 'url': 'https://assets.stagingeb.com/property_images/36549/127842/EB-C6549.jpg?version=1611968795'},
                                     {'title': None, 'url': 'https://assets.stagingeb.com/property_images/36549/127843/EB-C6549.jpg?version=1611968795'}],
                 'agent': None, 'features': []}


@ pytest.fixture()
def properties_page_resp():
    res = Response()
    res.code = "expired"
    res.error_type = "expired"
    res.status_code = 200
    res._content = b'{"content": {"dummydata": []}, \
                        "pagination": {"total": 100, \
                                        "limit": 10}}'
    return res


@ pytest.fixture()
def properties_bad_res(properties_page_resp):
    properties_page_resp.status_code = 404
    return properties_page_resp


@ pytest.fixture()
def test_client():
    app = create_app()
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


@ pytest.fixture()
def test_app():
    return create_app()


@ pytest.fixture()
def test_public_id(test_app):
    return test_app.config['EB_PROPERTY_PUBLIC_ID']


@ pytest.fixture()
def contact_form_data():
    form_data = {
        "name": "John Smith",
                "phone": "5559090909",
                "email": "mail@example.com",
                "property_id": "EB-XXXX01",
                "message": "I'm interested in this property. Please contact me.",
                "source": "mydomain.com"
    }
    return form_data


@ pytest.fixture()
def property_page_ok_response():
    res = Response()
    res.code = "expired"
    res.error_type = "expired"
    res.status_code = 200

    test_property_str = json.dumps(TEST_PROPERTY).encode('utf-8')
    res._content = test_property_str

    return res


@ pytest.fixture()
def property_contact_ok_response(contact_form_data):
    res = Response()
    res.status_code = 200

    test_property_contact = json.dumps(contact_form_data).encode('utf-8')
    res._content = test_property_contact

    return res
