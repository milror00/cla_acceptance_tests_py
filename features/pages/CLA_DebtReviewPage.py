from selenium.webdriver.common.by import By
from features.pages.SeleniumPage import SeleniumPage


class CLA_DebtReviewPage(SeleniumPage):

    def __init__(self, context):
        self.browser = context.browser

    def clickConfirm(self):
        self.click(By.XPATH, ".//*[contains(text(),'Confirm')]")

    @property
    def verifyOnPage(self):
        self.waitForPageLoaded(By.XPATH, ".//*[contains(text(),'Confirm')]")
        return True