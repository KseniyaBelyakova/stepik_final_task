import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    """Опции командной строки.
    В командную строку передается параметр вида '--language="es"'
    По умолчанию передается параметр, включающий язык en в браузере по дефолту
    """
    parser.addoption('--language', action='store', default='en', help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    # В переменную user_language передается параметр из командной строки
    user_language = request.config.getoption('language')
    if user_language is not None:
        options=Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        print("\nstart browser for test..")
    else:
        raise pytest.UsageError("--language should have correct locale code")
    yield browser
    print("\nquit browser..")
    browser.quit()



    
    