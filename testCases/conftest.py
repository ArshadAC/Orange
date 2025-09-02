import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options

@pytest.fixture()
def setup():
    driver = webdriver.Edge()
    driver.get("https://automation.credence.in/login")
    driver.maximize_window()
    return driver

# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture()
# def setup(browser):
#     if browser == 'edge':
#         print("Launching Edge browser")
#         driver = webdriver.Edge()
#     elif browser == 'firefox':
#         print("Launching FireFox browser")
#         driver = webdriver.Firefox()
#     else:
#         driver = webdriver.Edge()
#     driver.maximize_window()
#     yield driver
#     driver.quit()

def pytest_metadata(metadata):
    metadata["Project Name"] = "CredKart"
    metadata["Environment"] = "QA Environment"
    metadata["Module"] = "User Profile"
    metadata["Tester"] = "Pooja"
    metadata.pop("Plugins", None)


@pytest.fixture(params=[
    ("Rajeshp@gmail.com", "Rajesh@123", "Pass"),
    ("Rajeshp@gmail.com1", "Rajesh@123", "Fail"),
    ("Rajeshp@gmail.com", "Rajesh@1231", "Fail"),
    ("Rajeshp@gmail.com1", "Rajesh@1231", "Fail")
])

def getdataforlogin(request):
    return request.param


