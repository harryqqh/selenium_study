
# Viết 1 method tái sử dụng (api_helper) dùng cho API requests GET & POST, url: https://reqres.in/
import requests


class APIHelper():
    def test_get_user():
        response = requests.get('https://reqres.in/api/users/2')
        assert (response.status_code == 200), f'Expected status code 200 but got {response.status_code}'
        data = response.json()
        #print(data)#
        
    def test_post_user():
        payload = {
            "name": "John",
            "job": "Developer"
        }