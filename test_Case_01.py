import pytest


def test_numberOne(test_commonBrowser):
    print("This is Number One Test Case")
    assert test_commonBrowser == "Pass"



def test_numberTow(test_commonBrowser):
    print("This is Number Tow Test Case")



@pytest.mark.skip
def test_numberThree(test_commonBrowser):
    print("This is Number Three Test Case")
