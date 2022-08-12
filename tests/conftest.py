import pytest

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
