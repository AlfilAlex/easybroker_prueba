

def test_properties_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/properties' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/api/v1/properties')
    assert response.status_code == 200
