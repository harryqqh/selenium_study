# viet 1 method call API de su dung request Post & Get cho test scripts, url: https://reqres.in/

import requests
import pytest

class TestAPI:
    def test_get_user(self):
        response = requests.get('https://reqres.in/api/users/2')
        assert (response.status_code == 200), f'Expected status code 200 but got {response.status_code}'
        data =response.json()
        #print(response.json())#
        
    def test_post_user(self):
