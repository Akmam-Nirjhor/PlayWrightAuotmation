import pytest


@pytest.fixture(scope="module")
def preWork():
    print("I want to setup browser instance")

def test_instialCheck(preWork):
    print("This is first test")

def test_2ndIntialCheck(preWork):
    print("This is second test")

    list = [1,2,3,4,4,5]