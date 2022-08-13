from urllib import response
import pytest
from unittest.mock import Mock, patch


@pytest.mark.eb_api
def test_EB_API_get_response(test_client, test_public_id):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/properties' page is requested (GET)
    THEN check the EasyBreaker response is valid
    """
    response = test_client.get(f'/api/v1/properties/{test_public_id}')
    assert response.status_code == 200


@pytest.mark.eb_api
def test_EB_API_post_response(test_client, test_public_id, form_data):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/properties' page is requested (POST)
    THEN check the EasyBreaker response is valid
    """

    response = test_client.post(
        f'/api/v1/properties/{test_public_id}', data=form_data)
    assert response.status_code == 200


@patch('app.property.property.requests.get')
def test_property_profile(mock_get, property_page_ok_response, test_client, test_public_id):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/properties' page is requested (GET)
    THEN check the response is valid
    """
    mock_get.return_value = property_page_ok_response
    response = test_client.get(f'/api/v1/properties/{test_public_id}')

    assert response.status_code == 200


@patch('app.property.property.requests.post')
def test_property_contact(mock_get, property_contact_ok_response, test_public_id, test_client, form_data):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/properties' page is requested (POST)
    THEN check the response is valid
    """
    mock_get.return_value = property_contact_ok_response
    response = test_client.post(
        f'/api/v1/properties/{test_public_id}', data=form_data)

    assert response.status_code == 200
