from clients.api_client import APIClient

from helpers.auth_helper import login_user

def test_verify_authenticated_user_can_get_applications_updated():
    """
    Verify that an authenticated user can retrieve the applications list through the API client.
    """

    # make the api call with the token in the header
    get_applications_enpoint = f"/api/v1/applications"
    api_client = APIClient()
    response_body = api_client.get_json(get_applications_enpoint)

    # verify the api response body
    assert response_body, "Expected some date in response body but it was empty or None."
    assert isinstance(response_body, list), f"Expected the response body to be a list but got {type(response_body)}"
    