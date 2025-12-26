import pytest


@pytest.fixture(scope="session")
def test_commonBrowser():
    print("This Browser Instance Memory")
    return "Pass"

