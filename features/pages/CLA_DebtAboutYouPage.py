from selenium.webdriver.common.by import By
from features.pages.SeleniumPage import SeleniumPage



class CLA_DebtAboutYouPage(SeleniumPage):

    def __init__(self, context):
        self.browser = context.browser

    def clickContinueButton(self):
        self.click(By.XPATH, ".//*[@class='govuk-button']")

    def clickDoYouHaveAPartner_No(self):
        self.click(By.XPATH, ".//*[@id='have_partner-1']")

    def clickDoYouReceiveBenefits_No(self):
        self.click(By.XPATH, ".//*[@id='on_benefits-1']")

    def clickDoYouHaveChildrenUnder15_No(self):
        self.click(By.XPATH, ".//*[@id='have_children-1']")

    def clickHaveDependentChildrenOver16_No(self):
        self.click(By.XPATH, ".//*[@id='have_dependants-1']")

    def clickDoYouOwnAProperty_No(self):
        self.click(By.XPATH, ".//*[@id='own_property-1']")

    def clickAreYouEmployed_No(self):
        self.click(By.XPATH, ".//*[@id='is_employed-1']")

    def clickAreYouSelfEmployed_No(self):
        self.click(By.XPATH, ".//*[@id='is_self_employed-1']")

    def clickAreYouOrYourPartnerOver60_No(self):
        self.click(By.XPATH, ".//*[@id='aged_60_or_over-1']")

    def clickDoYouHaveSavingsOrInvestments_No(self):
        self.click(By.XPATH, ".//*[@id='have_savings-1']")

    def clickDoYouValuablesWorthOver500PoundsEach_No(self):
        self.click(By.XPATH, ".//*[@id='have_valuables-1']")

    @property
    def verifyOnPage(self):
        self.waitForPageLoaded(By.XPATH, "//*[contains(text(),'partner')]")
        return True
