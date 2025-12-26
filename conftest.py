import pytest


@pytest.fixture(scope="module")
def test_commonBrowser():
    print("This Browser Instance Memory")
    return "Pass"


@pytest.fixture(scope= "function")
def test_afterEffectedBrowseer():
    print("This is Secondary Browser Instance Memory")
    yield
    print("Tear Down Validation")






