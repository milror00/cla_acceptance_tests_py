from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumPage:

    def __init__(self, context):
        self.browser = context.browser

    def getURL(self, uri):
        self.browser.get(uri)

    def findElement(self, by, text):
        return self.browser.find_element(by, text)

    def click(self, by, text):
        element = self.findElement(by, text)
        element.click()

    def waitForPageLoaded(self, by, text):
        try:
            driver = self.browser
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((by, text))
            )
        except:
            raise
