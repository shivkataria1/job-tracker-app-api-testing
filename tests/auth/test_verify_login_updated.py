from clients.api_client import APIClient

api_client= APIClient()

def test_verify_user_can_login_with_valid_credentials():
    """
    Verify that a valid user can log in and receive a JWT token.
    """

    # Example response body:
    # {
    #   "access_token": "string",
    #   "token_type": "bearer",
    #   "expires_in": 0,
    #   "user": {
    #     "id": 0,
    #     "email": "user@example.com",
    #     "full_name": "string",
    #     "role": "user",
    #     "is_active": true,
    #     "created_at": "2026-10-30T10:57:29.045Z",
    #     "updated_at": "2026-10-30T10:57:29.045Z"
    #   }
    # }
    
    # make the call
    
    endpoint= f"/api/v1/auth/login"
    
    payload= {
         "email": "student@example.com",
         "password": "Password123!"
        }
    
    # the client will make the call and return the josn body of the response
    response_body= api_client.post_json(endpoint, data=payload)
    
    assert response_body["access_token"], f"Access token is required but got {response_body["access_token"]}"
    
    assert response_body["token_type"]== "bearer", "Token type is required"
    
    assert response_body["expires_in"], f"Expires in is required but got {response_body["expires_in"]}"
    
    assert response_body["user"], f"user is required but got {response_body['user']}"
    
    assert response_body["user"]["id"], f"user id is required but got {response_body['user']['id']}"
    
    assert response_body["user"]["email"]== payload["email"], f"user email is required but got {response_body['user']['email']}"
    
    assert response_body["user"]["full_name"], f"user full name is required but got {response_body['user']['full_name']}"
    
    assert response_body["user"]["role"], f"user role is required but got {response_body['user']['role']}"
    
    assert response_body["user"]["is_active"], f"user is active is required but got {response_body['user']['is_active']}"
    
    assert response_body["user"]["created_at"], f"user created at is required but got {response_body['user']['created_at']}"
    
    assert response_body["user"]["updated_at"], f"user updated at is required but got {response_body['user']['updated_at']}"
    
    
    
def test_verify_user_can_not_login_with_invalid_credentials():
    """
    Verify that invalid credentials are rejected with the expected error payload.
    """

    # Example response body:
    # {
    #   "error": {
    #     "code": "INVALID_CREDENTIALS",
    #     "message": "Invalid email or password",
    #     "details": []
    #   }
    # }
    
    # make the call
    endpoint= f"/api/v1/auth/login"
    
    payload= {
        "email": "student@example.com",
        "password": "Password123"
    }
    
    
    response_body= api_client.post_json(endpoint, data=payload, expected_status_code=401)
    
    assert isinstance(response_body["error"], dict), "Expected response body to have 'error' dictionary."
    
    assert response_body["error"]["code"]=="INVALID_CREDENTIALS", \
        f"Expected response error.code to be 'INVALID_CREDENTIALS', but got {response_body['error']['code']}"
        
    assert response_body["error"]["message"]=="Invalid email or password",\
        f"Expected error.message to be 'Invalid email or password', but got {response_body['error']['message']}"
        
    assert response_body["error"]["details"]==[],\
        f"Expected error.details to be '[]], but got {response_body['error']['details']}" 
    