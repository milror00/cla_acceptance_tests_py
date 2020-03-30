from selenium.webdriver.common.by import By
from features.pages.SeleniumPage import SeleniumPage


class CLA_DebtYoureLikelyToGetLegalAidPage(SeleniumPage):

    def __init__(self, context):
        self.browser = context.browser
