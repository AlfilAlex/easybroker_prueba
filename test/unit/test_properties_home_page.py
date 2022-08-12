from unittest.mock import Mock, patch
from requests import Response
from json import dumps

# from app.home.home import get_next_page
from wsgi import app


@patch('app.home.home.requests.get')
def test_getting_todos(mock_get):
    with app.app_context():
        from app.home.home import get_next_page

        res = Response()
        res.code = "expired"
        res.error_type = "expired"
        res.status_code = 400
        res._content = b'{"content": {"dummydata": []}, \
                            "pagination": {"total": 100, \
                                            "limit": 10}}'
        mock_get.return_value = res

        pagination, properties = get_next_page('muy_fakeeee_ggg_fake_url.com')

        assert pagination['total_pages'] == 10
        assert properties == {"dummydata": []}
