from selenium.webdriver.common.by import By
from features.pages.SeleniumPage import SeleniumPage


class CLA_ContactCentrePage(SeleniumPage):

    def __init__(self, context):
        self.browser = context.browser

    @property
    def verifyOnPage(self):
        self.waitForPageLoaded(By.XPATH, "//*[contains(text(),'you might qualify for legal aid')]")
        return True