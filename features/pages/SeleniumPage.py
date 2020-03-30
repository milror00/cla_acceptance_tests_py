from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from features.configuration.configuration import Configuration


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
            timeout = Configuration.getTimeOut(self)
            driver = self.browser
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, text))
            )
        except:
            raise

    def setText(self, by, byValue , text):
        element = self.findElement(by, byValue )
        element.clear()
        element.send_keys(text)

    def setSelectOptionByVisibleText(self, by , byValue, text):
         select = Select(self.findElement(by, byValue))
         select.select_by_visible_text(text)


