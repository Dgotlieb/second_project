import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.chrome
    yield driver


def test_pick_business_flow(setup):
    pass
