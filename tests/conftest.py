import pytest 

@pytest.fixture
def base_url():
    return 'http://172.17.0.1:8091'

@pytest.fixture
def info(base_url):
    return base_url+'/info'

@pytest.fixture
def bear(base_url):
    return base_url+'/bear'
