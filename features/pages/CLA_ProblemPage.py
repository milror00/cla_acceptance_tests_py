from features.pages.SeleniumPage import SeleniumPage
from selenium.webdriver.common.by import By


class CLA_ProblemPage(SeleniumPage):

    def __init__(self, context):
        self.browser = context.browser

    def clickDebt(self):
        self.click(By.XPATH, ".//*[@class='cla-scope-options-list']/li[3]/a")


    @property
    def verifyOnPage(self):
        self.waitForPageLoaded(By.XPATH,"//*[contains(text(),'Debt')]")
        return True
