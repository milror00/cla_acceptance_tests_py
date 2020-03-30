from selenium.webdriver.common.by import By
from features.pages.SeleniumPage import SeleniumPage



class CLA_DebtChooseProblemPage(SeleniumPage):

    def __init__(self, context):
        self.browser = context.browser

    def clickYouAreHomeOwnerAtRisk(self):
        self.click(By.XPATH, ".//*[@class='cla-scope-options-list']/li[1]/a")

    @property
    def verifyOnPage(self):
        self.waitForPageLoaded(By.XPATH, "//*[contains(text(),'home owner')]")
        return True
