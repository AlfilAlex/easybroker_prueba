import pytest
import requests

from unittest.mock import Mock, patch
from requests import Response
from json import dumps


@patch('app.home.home.requests.get')
def test_get_next_page_ok(mock_get, test_app, properties_page_resp):
    '''
    GIVEN a properties page
    WHEN some acces to /properties page
    THEN check if EP handle ok responses from EasyBraker API
    '''
    with test_app.app_context():
        from app.home.home import get_next_page

        mock_get.return_value = properties_page_resp
        pagination, properties = get_next_page('url_100%_real_no_fake.com')

        assert pagination['total_pages'] == 10
        assert properties == {"dummydata": []}


@patch('app.home.home.requests.get')
def test_get_next_page_fail(mock_get, test_app, properties_bad_res):
    '''
    GIVEN a properties page
    WHEN some acces to /properties page
    THEN check if EP handle not_ok responses from EasyBraker API
    '''
    with test_app.app_context():
        from app.home.home import get_next_page

        mock_get.return_value = properties_bad_res

        with pytest.raises(requests.exceptions.HTTPError):
            pagination, properties = get_next_page('url_100%_real_no_fake.com')
