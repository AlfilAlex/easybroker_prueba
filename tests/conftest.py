import pytest
from app import create_app
from wsgi import app
from requests import Response


@pytest.fixture()
def new_properties_page():
    res = Response()
    res.code = "expired"
    res.error_type = "expired"
    res.status_code = 200
    res._content = b'{"content": {"dummydata": []}, \
                        "pagination": {"total": 100, \
                                        "limit": 10}}'
    return res


@pytest.fixture()
def new_properties_page_not_ok(new_properties_page):
    new_properties_page.status_code = 404
    return new_properties_page


@pytest.fixture()
def test_client():
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


@pytest.fixture()
def test_app():
    return create_app()


@pytest.fixture()
def test_public_id(test_client, test_app):
    return test_app.config['EB_PROPERTY_PUBLIC_ID']
