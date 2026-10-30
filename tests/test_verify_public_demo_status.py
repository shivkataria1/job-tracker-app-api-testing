
import requests

from configs.settings import BASE_URL

def test_verify_public_status():
    
    
    """
    Example response body:
      {
  "total_seeded_applications": 4,
  "status_counts": {
    "potential": 2,
    "applied": 1,
    "in_progress": 1,
    "final_stage": 0,
    "hired": 0,
    "rejected": 0,
    "withdrawn": 0,
    "total": 4
  }
}  
    """
    
    #make the call
    
    url= f"{BASE_URL}/api/v1/public/demo-stats"
    response= requests.get(url)
    
    
    
    #verify the status_code
    
    status_code=response.status_code
    assert status_code==200, f"API /api/v1/public/demo-stats is not returning a 200 status code.Actual status code: {status_code}"
    

    
    #verify the response body
    
    response_body=response.json()
    
    # verify the number of keys is correct type.
    assert len(response_body.keys())==2, f"The number of keys expected is 2 but the actula keeys are {response_body.keys()}"
    
    # verify the values are of the corret type.
    assert isinstance(response_body["total_seeded_applications"],int), f"The total_seeded_applications expected is an integer but the actual value is {response_body["total_seeded_applications"]}"
    #assert response_body["total_seeded_applications"] ==4
    assert isinstance(response_body["status_counts"], dict), f"The status_counts expected is dictionary but the actual value is {response_body["status_counts"]}"
    
    # verify the status_counts keys are correct.
    status_counts=response_body["status_counts"]
    for k, v in status_counts.items():
        #print(f"Key:{k}, Value:{v}")
        assert isinstance(v, int), f"The expected value is an integer but the actula value is{v}"
    
    # assert response_body["potential"]== 2
    # assert response_body["applied"]==1
    # assert response_body["in_progress"]== 1
    # assert response_body["final_stage"]== 0
    # assert response_body["hired"]== 0
    # assert response_body["rejected"]== 0
    # assert response_body["withdrawn"]== 0
    # assert response_body["total"]== 4