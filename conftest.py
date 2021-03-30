import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):

    #get/set language parameter
    options = Options()
    language = request.config.getoption("language")
    browser = None
    if language:
        print("\nlanguage was selected")
        user_language = language
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        print("\nlanguage was NOT selected (en - by default)")
        browser = webdriver.Chrome()

    #find each element min 5 sec
    browser.implicitly_wait(5)
    
    yield browser
    print("\nquit browser..")
    browser.quit()
