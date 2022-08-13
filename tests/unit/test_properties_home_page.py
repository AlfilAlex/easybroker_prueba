import pytest
import requests

from unittest.mock import Mock, patch
from requests import Response
from json import dumps
from tests.conftest import new_properties_page

# from app.home.home import get_next_page
# from wsgi import app


@patch('app.home.home.requests.get')
def test_get_next_page_ok(mock_get, test_app, new_properties_page):
    '''
    GIVEN a properties page
    WHEN some acces to /properties page
    THEN check if EP handle ok responses from EasyBraker API
    '''
    with test_app.app_context():
        from app.home.home import get_next_page

        mock_get.return_value = new_properties_page
        pagination, properties = get_next_page('url_100%_real_no_fake.com')

        assert pagination['total_pages'] == 10
        assert properties == {"dummydata": []}


@patch('app.home.home.requests.get')
def test_get_next_page_fail(mock_get, test_app, new_properties_page_not_ok):
    '''
    GIVEN a properties page
    WHEN some acces to /properties page
    THEN check if EP handle not_ok responses from EasyBraker API
    '''
    with test_app.app_context():
        from app.home.home import get_next_page

        mock_get.return_value = new_properties_page_not_ok

        with pytest.raises(requests.exceptions.HTTPError):
            pagination, properties = get_next_page('url_100%_real_no_fake.com')
