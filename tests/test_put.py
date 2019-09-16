import requests

begin_param = {"bear_type":"POLAR","bear_name":"MISHA","bear_age":13}
new_param = {"bear_id":5,"bear_type":"BLACK","bear_name":"mikhail","bear_age":17.5}
test_answ = {"bear_id":5,"bear_type":"BLACK","bear_name":"mikhail","bear_age":17.5}

class TestPutBear(object):
    def test_post_polar(self, bear):
        requests.post(url=bear, json=begin_param)
        requests.put(url=bear+"/1", json=new_param)
        response = requests.get(url=bear)
        assert response.status_code == 200
        assert response.json() == [test_answ]
        
