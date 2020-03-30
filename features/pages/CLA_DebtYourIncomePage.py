from selenium.webdriver.common.by import By
from features.pages.SeleniumPage import SeleniumPage


class CLA_DebtYourIncomePage(SeleniumPage):

    def __init__(self, context):
        self.browser = context.browser

    def setYourIncome(self,text):
        self.setText(By.XPATH,".//*[@id='your_income-maintenance-per_interval_value']" ,text)

    def setYourIncomeInterval(self,text):
        self.setSelectOptionByVisibleText( By.XPATH, ".//*[@id='your_income-maintenance-interval_period']", text)

    def setYourPension(self, text):
        self.setText(By.XPATH, ".//*[@id='your_income-pension-per_interval_value']",  text)

    def setYourPensionInterval(self, text):
        self.setSelectOptionByVisibleText(By.XPATH, ".//*[@id='your_income-pension-interval_period']", text)

    def setAnyOtherIncome(self, text):
        self.setText(By.XPATH, ".//*[@id='your_income-other_income-per_interval_value']", text)

    def setAnyOtherIncomeInterval(self, text):
        self.setSelectOptionByVisibleText(By.XPATH,".//*[@id='your_income-other_income-interval_period']", text)

    def clickContinue(self):
        self.click(By.XPATH, ".//*[@class='govuk-button']" )


    @property
    def verifyOnPage(self):
        self.waitForPageLoaded(By.XPATH, "//*[contains(text(),'Maintenance')]")
        return True