from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from features.configuration.configuration import Configuration


@fixture
def selenium_browser(context):
    # -- HINT: @behave.fixture is similar to @contextlib.contextmanager
    config = Configuration()
    if config.getBrowserType() == "FIREFOX":
        firefox_binary = FirefoxBinary('/usr/bin/firefox')
        context.browser = webdriver.Firefox(firefox_binary=firefox_binary)
    yield context.browser
    # -- CLEANUP-FIXTURE PART:
    context.browser.quit()


def before_all(context):
    use_fixture(selenium_browser, context)
