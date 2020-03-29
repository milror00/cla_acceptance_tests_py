from features.pages.SeleniumPage import SeleniumPage
from selenium.webdriver.common.by import By

class CLA_LegalAidIsAvailablePage(SeleniumPage):

    def __init__(self, context):
        self.browser = context.browser

    def clickCheckIfYouQualifyLink(self):
        self.click(By.XPATH, ".//*[@class='govuk-grid-column-two-thirds']/a[1]")

    @property
    def verifyOnPage(self):
        self.waitForPageLoaded(By.XPATH,".//*[@class='govuk-grid-column-two-thirds']/a[1]")
        return True