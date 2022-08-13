def test_property_page(test_client, test_public_id):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/properties' page is requested (GET)
    THEN check the response is valid
    """
    print('[ [ [ [ [ [ [ ')
    print(test_public_id)
    print('] ] ] ] ] ] ]')
    response = test_client.get('/api/v1/properties/{test_public_id}')
    assert response.status_code == 200


def test_property_contact(test_client, test_public_id):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/properties' page is requested (GET)
    THEN check the response is valid
    """

    response = test_client.post('/api/v1/properties/{test_public_id}')
    assert response.status_code == 200
