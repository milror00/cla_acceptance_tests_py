from behave import given, when, then
import unittest
from features.configuration.configuration import Configuration
from features.pages.CLA_DebtYourIncomePage import CLA_DebtYourIncomePage
from features.pages.CLA_StartPage import CLA_WebstartPage
from features.pages.CLA_ProblemPage import CLA_ProblemPage
from features.pages.CLA_DebtChooseProblemPage import CLA_DebtChooseProblemPage
from features.pages.CLA_LegalAidIsAvailablePage import CLA_LegalAidIsAvailablePage
from features.pages.CLA_DebtAboutYouPage import CLA_DebtAboutYouPage
from features.pages.CLA_DebtYourOutgoingsPage import CLA_DebtYourOutgoingsPage
from features.pages.CLA_DebtReviewPage import CLA_DebtReviewPage
from features.pages.CLA_LegalAidIsNotAvailablePage import CLA_LegalAidIsNotAvailablePage
from features.pages.CLA_CallContactCentrePage import CLA_ContactCentrePage

@given(u'I am on debt page')
def step_impl(context):
    config = Configuration()
    page = CLA_WebstartPage(context)
    page.getURL(config.getBaseURI())
    page.clickStartNow()
    debtPage = CLA_ProblemPage(context)
    debtPage.verifyOnPage
    debtPage.clickDebt()

@when(u'I click that I am at risk of loosing my home')
def step_impl(context):
    page = CLA_DebtChooseProblemPage(context)
    page.verifyOnPage
    page.clickYouAreHomeOwnerAtRisk()


@when(u'I click check if I qualify')
def step_impl(context):
    page = CLA_LegalAidIsAvailablePage(context)
    page.verifyOnPage
    page.clickCheckIfYouQualifyLink()


@when(u'answer No to Do You have a partner?')
def step_impl(context):
    page = CLA_DebtAboutYouPage(context)
    page.verifyOnPage
    page.clickDoYouHaveAPartner_No()


@when(u'answer No to Do you receive any benefits (including Child Benefit)?')
def step_impl(context):
    page = CLA_DebtAboutYouPage(context)
    page.verifyOnPage
    page.clickDoYouReceiveBenefits_No()


@when(u'answer No to Do you have any children aged 15 or under?')
def step_impl(context):
    page = CLA_DebtAboutYouPage(context)
    page.verifyOnPage
    page.clickDoYouHaveChildrenUnder15_No()



@when(u'answer No to Do you have any dependants aged 16 or over?')
def step_impl(context):
    page = CLA_DebtAboutYouPage(context)
    page.verifyOnPage
    page.clickHaveDependentChildrenOver16_No()



@when(u'answer No to Do you own any property?')
def step_impl(context):
    page = CLA_DebtAboutYouPage(context)
    page.verifyOnPage
    page.clickDoYouOwnAProperty_No()



@when(u'answer No to Are you employed?')
def step_impl(context):
    page = CLA_DebtAboutYouPage(context)
    page.verifyOnPage
    page.clickAreYouEmployed_No()



@when(u'answer No to Are you self-employed?')
def step_impl(context):
    page = CLA_DebtAboutYouPage(context)
    page.verifyOnPage
    page.clickAreYouSelfEmployed_No()



@when(u'answer No to Are you or your partner (if you have one) aged 60 or over?')
def step_impl(context):
    page = CLA_DebtAboutYouPage(context)
    page.verifyOnPage
    page.clickAreYouOrYourPartnerOver60_No()



@when(u'answer No to Do you have any savings or investments?')
def step_impl(context):
    page = CLA_DebtAboutYouPage(context)
    page.verifyOnPage
    page.clickDoYouHaveSavingsOrInvestments_No()



@when(u'answer No to Do you have any valuable items worth over £500 each?')
def step_impl(context):
    page = CLA_DebtAboutYouPage(context)
    page.verifyOnPage
    page.clickDoYouValuablesWorthOver500PoundsEach_No()



@when(u'I click continue to Your money coming in page')
def step_impl(context):
    page = CLA_DebtAboutYouPage(context)
    page.verifyOnPage
    page.clickContinueButton()


@when(u'answer {number:d} to your maintenance received')
def step_impl(context, number):
    page = CLA_DebtYourIncomePage(context)
    page.verifyOnPage
    page.setYourIncome(str(number))


@when(u'answer "{text}" to your maintenance frequency')
def step_impl(context, text):
    page = CLA_DebtYourIncomePage(context)
    page.verifyOnPage
    page.setYourIncomeInterval(text)


@when(u'answer {number:d} to your pension received')
def step_impl(context, number):
    page = CLA_DebtYourIncomePage(context)
    page.verifyOnPage
    page.setYourPension(str(number))


@when(u'answer "{text}" to your pension frequency')
def step_impl(context, text):
    page = CLA_DebtYourIncomePage(context)
    page.verifyOnPage
    page.setYourPensionInterval(text)


@when(u'answer {number:d} to your other income')
def step_impl(context, number):
    page = CLA_DebtYourIncomePage(context)
    page.verifyOnPage
    page.setAnyOtherIncome(str(number))


@when(u'answer "{text}" to your other income frequency')
def step_impl(context, text):
    page = CLA_DebtYourIncomePage(context)
    page.verifyOnPage
    page.setAnyOtherIncomeInterval(text)


@when(u'I click continue to Your outgoings page')
def step_impl(context):
    page = CLA_DebtYourIncomePage(context)
    page.verifyOnPage
    page.clickContinue()


@when(u'answer {number:d} to your rent amount')
def step_impl(context, number):
    page = CLA_DebtYourOutgoingsPage(context)
    page.verifyOnPage
    page.setRent(str(number))



@when(u'answer "{text}" to your rent schedule')
def step_impl(context, text):
    page = CLA_DebtYourOutgoingsPage(context)
    page.verifyOnPage
    page.setRentInterval(text)


@when(u'answer {number:d} to your maintenance payment')
def step_impl(context, number):
    page = CLA_DebtYourOutgoingsPage(context)
    page.verifyOnPage
    page.setMaintenance(str(number))


@when(u'answer "{text}" to your maintenance payment schedule')
def step_impl(context, text):
    page = CLA_DebtYourOutgoingsPage(context)
    page.verifyOnPage
    page.setMaintenanceInterval(text)


@when(u'answer {number:d} to your monthly income contribution order')
def step_impl(context, number):
    page = CLA_DebtYourOutgoingsPage(context)
    page.verifyOnPage
    page.setIncomeContribution(str(number))


@when(u'I click continue to review the answers page')
def step_impl(context):
    page = CLA_DebtYourOutgoingsPage(context)
    page.verifyOnPage
    page.clickReviewYourAnswers()


@when(u'I click reviewed answers')
def step_impl(context):
    page = CLA_DebtReviewPage(context)
    page.verifyOnPage
    page.clickConfirm()


@then(u'I get confirmed my eligibity is {text}')
def step_impl(context,text):
    if text == 'eligible':
        print("eligible")
        page = CLA_ContactCentrePage(context)
        page.verifyOnPage
        return True
    else:
        page1 = CLA_LegalAidIsNotAvailablePage(context)
        page1.verifyOnPage
        return False
