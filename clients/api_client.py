"""Reusable HTTP client for the job-tracker API.

This module centralizes common authentication and request behavior so tests can
focus on API assertions instead of repeating login and header setup logic.
"""

import logging

import requests

from configs.settings import BASE_URL, DEFUALT_USER_EMAIL, DEFUALT_USER_PASSWORD

logger = logging.getLogger(__name__)


class APIClient:
    """Wrapper around the public API used by tests.

    The client automatically logs in when created in authenticated mode and stores
    the bearer token in the request headers for future API calls.
    """
    
    def __init__(self, authenticated=True, email=DEFUALT_USER_EMAIL, password=DEFUALT_USER_PASSWORD):
        
        self.headers={}
        self.authenticated=authenticated
        logger.info("Initializing APIClient (authenticated=%s)", authenticated)
        
        if authenticated:
            logger.debug("Starting login flow for user=%s", email)
            access_token=self.login(email, password)
            self.headers["Authorization"] = f"Bearer {access_token}"
            logger.info("Authentication header configured for user=%s", email)
            
    
    def login(self, email, password):
        """Authenticate a user and return the access token.

        Args:
            email: Email address used for login.
            password: Password used for login.

        Returns:
            The access token returned by the API.
        """
        url = f"{BASE_URL}/api/v1/auth/login"
        logger.info("Attempting login for user=%s", email)
                    
        payload= {
            "email": email,
            "password": password
            }
        logger.debug("Login payload prepared for user=%s", email)

        try:
            response_body = self.post_json("/api/v1/auth/login", data=payload)
        except AssertionError:
            logger.error("Login failed for user=%s", email)
            raise
                    
        logger.info("Login successful for user=%s", email)
        return response_body["access_token"]
        
    
    
    def get(self, endpoint ,headers=None, expected_status_code=200):
        """Send a GET request to an API endpoint.

        Args:
            endpoint: Relative API path such as "/api/v1/applications".
            headers: Extra request headers to merge with auth headers.
            expected_status_code: HTTP status code expected for a successful call.

        Returns:
            The raw requests.Response object.
        """
        
        headers= self.build_headers(headers)
        url =self.build_url(endpoint)
        logger.debug("GET %s", url)
        response = requests.get(url, headers=headers)
        logger.info("GET %s -> %s", url, response.status_code)
        self.verify_status_code(response, expected_status_code, url)
        return response
    
    def get_json(self, endpoint, headers=None, expected_status_code=200):
        """Send a GET request and return the JSON response body.

        This is the common helper for endpoints that return structured JSON data.
        """
        headers= self.build_headers(headers)
        response= self.get(endpoint, headers, expected_status_code)
        
        return response.json()
    
     
     
    def post(self, endpoint, data, headers=None, expected_status_code=200):
        """Send a POST request with JSON data.

        Args:
            endpoint: Relative API path such as "/api/v1/auth/login".
            data: JSON payload to send in the request body.
            headers: Extra request headers to merge with auth headers.
            expected_status_code: HTTP status code expected for a successful call.

        Returns:
            The raw requests.Response object.
        """
        headers= self.build_headers(headers)
        url =self.build_url(endpoint)
        logger.debug("POST %s", url)
         
        response= requests.post(url, json=data, headers=headers)
        logger.info("POST %s -> %s", url, response.status_code)
        self.verify_status_code(response, expected_status_code, url)
        return response
            
    
    def post_json(self, endpoint, data, headers=None,expected_status_code=200):
        """Send a POST request and return the parsed JSON response body.

        This helps tests validate API payloads without manually decoding responses.
        """
        headers= self.build_headers(headers)
        
        response=self.post(endpoint, data, headers, expected_status_code)
        
        return response.json()
    
    
    def build_headers(self, headers=None):
        """Combine stored auth headers with any custom request headers.

        This keeps authentication centralized and ensures each API call uses the
        same bearer token unless a specific request overrides it.
        """
        
        if self.authenticated:
            logger.debug("Merging auth headers for authenticated request")
            return {**self.headers, **(headers or {})} # combining two dictionaries
        
        logger.debug("Returning request headers without auth")
        return headers
    
    
    def verify_status_code(self, response, expected_status_code, url):
        """Assert that an HTTP response matches the expected status code.

        This keeps response validation consistent across all methods and gives a
        clear failure message when an API contract changes.
        """
        assert response.status_code== expected_status_code, \
            f"Status Code. Expected: {expected_status_code}, \
            Actual: {response.status_code}, URL: {url}"
        logger.debug("Status code verification passed for %s: %s", url, response.status_code)
            
    
    def build_url(self, endpoint):
        """Join the configured base URL with a relative endpoint."""
        
        return f"{BASE_URL}{endpoint}"
        
    
     
        
        