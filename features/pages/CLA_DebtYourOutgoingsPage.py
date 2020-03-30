from selenium.webdriver.common.by import By
from features.pages.SeleniumPage import SeleniumPage


class CLA_DebtYourOutgoingsPage(SeleniumPage):

    def __init__(self, context):
        self.browser = context.browser

    def setRent(self,text):
        self.setText(By.XPATH,".//*[@id='rent-per_interval_value']" ,text)

    def setRentInterval(self,text):
        self.setSelectOptionByVisibleText( By.XPATH, ".//*[@id='rent-interval_period']", text)

    def setMaintenance(self, text):
        self.setText(By.XPATH, ".//*[@id='maintenance-per_interval_value']",  text)

    def setMaintenanceInterval(self, text):
        self.setSelectOptionByVisibleText(By.XPATH, ".//*[@id='maintenance-interval_period']", text)

    def setIncomeContribution(self, text):
        self.setText(By.XPATH, ".//*[@id='income_contribution']", text)


    def clickReviewYourAnswers(self):
        self.click(By.XPATH, ".//*[@class='govuk-button']" )

    @property
    def verifyOnPage(self):
        self.waitForPageLoaded(By.XPATH, "//*[contains(text(),'Rent')]")
        return True