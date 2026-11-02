
from clients.api_client import APIClient

from helpers.auth_helper import login_user

def test_verify_authenticated_user_can_get_applications_summary_updated():
    """
    Verify that the summary API returns integer counts for each application status bucket.
    """

    # make the call with the token in header
    get_applications_summary_endpoint = f"/api/v1/applications/summary"
    api_client = APIClient()
    response_body = api_client.get_json(get_applications_summary_endpoint)

    assert response_body, "Expected some date in response body but it was empty or None. Endpoint: api/v1/applications/summary"
    assert isinstance(response_body["potential"], int), f"Expected integer in the response body 'potential' field. But got {response_body['potential']}"
    assert isinstance(response_body["applied"], int), f"Expected integer in the response body 'potential' field. But got {response_body['applied']}"
    assert isinstance(response_body["in_progress"], int), f"Expected integer in the response body 'potential' field. But got {response_body['in_progress']}"
    assert isinstance(response_body["final_stage"], int), f"Expected integer in the response body 'potential' field. But got {response_body['final_stage']}"
    assert isinstance(response_body["hired"], int), f"Expected integer in the response body 'potential' field. But got {response_body['hired']}"
    assert isinstance(response_body["rejected"], int), f"Expected integer in the response body 'potential' field. But got {response_body['rejected']}"
    assert isinstance(response_body["withdrawn"], int), f"Expected integer in the response body 'potential' field. But got {response_body['withdrawn']}"
    assert isinstance(response_body["total"], int), f"Expected integer in the response body 'potential' field. But got {response_body['total']}"