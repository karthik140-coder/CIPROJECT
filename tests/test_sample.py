import os

def test_addition():
    assert 1 + 1 == 2

def test_addition_fail():
    assert 1 + 1 == 3

def test_base_url():
    base_url = os.getenv("BASE_URL")
    assert base_url is not None