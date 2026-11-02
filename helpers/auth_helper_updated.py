
from clients.api_client import APIClient

from configs.settings import DEFUALT_USER_EMAIL, DEFUALT_USER_PASSWORD

def login_user(email=DEFUALT_USER_EMAIL, password=DEFUALT_USER_PASSWORD):
    
     # get JWT token.
     # login with user and get the token from the response
        
     # make the call
            
            endpoint= f"/api/v1/auth/login"
            
            payload= {
                 "email": email,
                 "password": password
                }
            
            api_client = APIClient()
            
            response_body= api_client.post_json(endpoint, data=payload)
            
            return response_body["access_token"]
        