from selenium.webdriver.common.by import By
from features.pages.SeleniumPage import SeleniumPage


class CLA_LegalAidIsNotAvailablePage(SeleniumPage):

    def __init__(self, context):
        self.browser = context.browser

    @property
    def verifyOnPage(self):
        self.waitForPageLoaded(By.XPATH, "//*[contains(text(),'Disposable income')]")
        return True