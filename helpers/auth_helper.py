
import requests

from configs.settings import BASE_URL, DEFUALT_USER_EMAIL, DEFUALT_USER_PASSWORD

def login_user(email=DEFUALT_USER_EMAIL, password=DEFUALT_USER_PASSWORD):
    
     # get JWT token.
     # login with user and get the token from the response
        
     # make the call
            
            url= f"{BASE_URL}/api/v1/auth/login"
            
            payload= {
                 "email": email,
                 "password": password
                }
            
            response= requests.post(url, json=payload)
            
            assert response.status_code==200, f"Expected status code 200, but actula code {response.status_code}"
            
            response_body= response.json()
            
            
            return response_body["access_token"]
        