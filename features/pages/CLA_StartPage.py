from selenium.webdriver.common.by import By
from features.pages.SeleniumPage import SeleniumPage

class CLA_WebstartPage(SeleniumPage):

    def __init__(self, context):
        self.browser = context.browser

    def clickStartNow(self):
        self.click(By.CLASS_NAME, "govuk-button--start")
