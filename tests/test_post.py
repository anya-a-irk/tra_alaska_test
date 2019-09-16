import requests

test_param = {"bear_type":"POLAR","bear_name":"MISHA","bear_age":13}
test_answ = {"bear_id":1,"bear_type":"POLAR","bear_name":"MISHA","bear_age":13}

class TestPostBear(object):
    def test_answer(self, info):
        response = requests.get(info)
        assert response.status_code == 200
        
    def test_post_polar(self, bear):
        test_param["bear_type"] = test_answ["bear_type"] = "POLAR"
        test_answ["bear_id"] = 1
        response = requests.post(url=bear, json=test_param)
        assert response.status_code == 200
        response = requests.get(url=bear)
        assert response.json() == [test_answ]
        
    def test_post_black(self, bear):
        test_param["bear_type"] = test_answ["bear_type"] = "BLACK"
        test_answ["bear_id"] = 2
        requests.delete(url = bear)
        response = requests.post(url=bear, json=test_param)
        assert response.status_code == 200
        response = requests.get(url=bear)
        assert response.json() == [test_answ]

    def test_post_gummy(self, bear):
        test_param["bear_type"] = test_answ["bear_type"] = "GUMMY"
        test_answ["bear_id"] = 3
        requests.delete(url = bear)
        response = requests.post(url=bear, json=test_param)
        assert response.status_code == 200
        response = requests.get(url=bear)
        assert response.json() == [test_answ]
        
    def test_post_brown(self, bear):
        test_param["bear_type"] = test_answ["bear_type"] = "BROWN"
        test_answ["bear_id"] = 4
        requests.delete(url = bear)
        response = requests.post(url=bear, json=test_param)
        assert response.status_code == 200
        response = requests.get(url=bear)
        assert response.json() == [test_answ]
        
