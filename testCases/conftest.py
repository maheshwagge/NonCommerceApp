import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as chromeservice
from webdriver_manager.chrome import ChromeDriverManager




@pytest.fixture()
def setup(browser, request):
    global driver
    if browser == 'chrome':
        driver = webdriver.Chrome(service=chromeservice(ChromeDriverManager().install()))
        print("Launching chrome browser.........")
    elif browser == 'firefox':
        driver = webdriver.Firefox("Driver/geckodriver-v0.31.0-win64/geckodriver.exe")
        print("Launching firefox browser.........")
    request.cls.driver = driver
    driver.get("https://www.google.co.in/")
    yield
    driver.close()
def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")



@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")
#
#
# ########### pytest HTML Report ################
#
# # It is hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata['Project Name'] = 'nop Commerce'
#     config._metadata['Module Name'] = 'Customers'
#     config._metadata['Tester'] = 'Mahesh'
#
#
# # It is hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)
