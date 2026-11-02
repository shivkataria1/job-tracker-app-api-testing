
import requests
from configs.settings import BASE_URL
from helpers.auth_helper import login_user

def test_verify_authenticated_user_can_get_applications_summary():
    """
    Verify that the applications summary endpoint returns the expected aggregate counts.
    """

    # login and get JWT token.
    access_token = login_user()

    # make the call with the token in header
    get_applications_url = f"{BASE_URL}/api/v1/applications/summary"
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(get_applications_url, headers=headers)

    # verify the status code
    assert response.status_code == 200, \
        f"Get applications/summary api response expected to be 200 but actual was {response.status_code} Endpoint: 'api/v1/applications/summary'"

    # verify the response body
    response_body = response.json()
    assert response_body, "Expected some date in response body but it was empty or None. Endpoint: api/v1/applications/summary"
    assert isinstance(response_body["potential"], int), f"Expected integer in the response body 'potential' field. But got {response_body['potential']}"
    assert isinstance(response_body["applied"], int), f"Expected integer in the response body 'potential' field. But got {response_body['applied']}"
    assert isinstance(response_body["in_progress"], int), f"Expected integer in the response body 'potential' field. But got {response_body['in_progress']}"
    assert isinstance(response_body["final_stage"], int), f"Expected integer in the response body 'potential' field. But got {response_body['final_stage']}"
    assert isinstance(response_body["hired"], int), f"Expected integer in the response body 'potential' field. But got {response_body['hired']}"
    assert isinstance(response_body["rejected"], int), f"Expected integer in the response body 'potential' field. But got {response_body['rejected']}"
    assert isinstance(response_body["withdrawn"], int), f"Expected integer in the response body 'potential' field. But got {response_body['withdrawn']}"
    assert isinstance(response_body["total"], int), f"Expected integer in the response body 'potential' field. But got {response_body['total']}"