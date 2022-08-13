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
def new_properties_page():
    res = Response()
    res.code = "expired"
    res.error_type = "expired"
    res.status_code = 200
    res._content = b'{"content": {"dummydata": []}, \
                        "pagination": {"total": 100, \
                                        "limit": 10}}'
    return res


@ pytest.fixture()
def new_properties_page_not_ok(new_properties_page):
    new_properties_page.status_code = 404
    return new_properties_page


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
def form_data():
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
def property_contact_ok_response():
    res = Response()
    res.status_code = 200

    return res


'''
{'public_id': 'EB-XXXXX', 'title': 'Departamento Fonda de Eduviges',
'description': 'Casa de varios cuartos sin iluminación y con almas perdidas',
'location': {'name': 'Del Valle Oriente, San Pedro Garza García, Nuevo León', 'latitude': 0.0, 'longitude': 0.0},
'property_type': 'Departamento', 'created_at': '2021-01-29T18:57:04-06:00',
'updated_at': '2022-08-07T14:25:35-05:00', 'published_at': '2022-08-07T14:25:35-05:00',
'operations': [{'type': 'rental', 'amount': 48000.0, 'currency': 'MXN', 'formatted_amount': '$48,000', 'commission': {'type': 'percentage'}, 'unit': 'total'}],
'public_url': 'https://www.stagingeb.com/mx/inmueble/departamento-en-renta-en-valle-oriente-en-san-pedro-garza-garcia-f76dd649-7aea-4756-9674-2412ac8e7cfa',
'tags': [], 'show_prices': True, 'share_commission': False,
'property_images': [{'title': None, 'url': 'https://assets.stagingeb.com/property_images/36549/127842/EB-C6549.jpg?version=1611968795'},
{'title': None, 'url': 'https://assets.stagingeb.com/property_images/36549/127843/EB-C6549.jpg?version=1611968795'},
'agent': None, 'features': []}


'''
