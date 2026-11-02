import os

# Base_URL ->  the url does not include any endpoint  

# which will change per environment 
# https://dev.jobtracking.com
# https://staging.jobtracking.com
# http://localhost:3050


BASE_URL= os.getenv("BASE_URL", "http://localhost:3050")

DEFUALT_USER_EMAIL= os.getenv("DEFUALT_USER_EMAIL", "student@example.com")

DEFUALT_USER_PASSWORD= os.getenv("DEFUALT_USER_PASSWORD", "Password123!")