from features.pages.SeleniumPage import SeleniumPage
from selenium.webdriver.common.by import By

class CLA_DebtYoureLikelyToGetLegalAidPage(SeleniumPage):


    def __init__(self, context):
        self.browser = context.browser

    