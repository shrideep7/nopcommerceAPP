from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':

        driver = webdriver.Chrome()
        print("launching chrome browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching firefox browser")
    elif browser == 'edge':
        driver = webdriver.Edge()
        print('launching edge browser')
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


########################  pyetest HTML report ########################

def pytest_configure(config):
    config._metadata['Project Name'] = 'nop commerce'
    config._metadata['Module Name'] = 'Custmoers'
    config._metadata['Tester'] = 'Shridhar'
