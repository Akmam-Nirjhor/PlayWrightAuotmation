import pytest


@pytest.fixture
def test_commonBrowser():
    print("This is my Browser")

def test_NumberOne(test_commonBrowser):
    print("This is my Number One Test Case")
