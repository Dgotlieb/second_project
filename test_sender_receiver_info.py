import pytest
from selenium import webdriver


@pytest.fixture
def setup():
    driver = webdriver.chrome
    yield driver


def test_sender_receiver_info_flow(setup):
    pass
