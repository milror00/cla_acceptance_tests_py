from behave import given, when, then
from features.configuration.configuration import Configuration
from features.pages.CLA_StartPage import CLA_WebstartPage
from features.pages.CLA_ProblemPage import CLA_ProblemPage
from features.pages.CLA_DebtChooseProblemPage import CLA_DebtChooseProblemPage
from features.pages.CLA_LegalAidIsAvailablePage import CLA_LegalAidIsAvailablePage
from features.pages.CLA_DebtAboutYouPage import CLA_DebtAboutYouPage


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


@when(u'answer 0 to your maintenance received')
def step_impl(context):
    raise NotImplementedError(u'STEP: When answer 0 to your mainetnance received')


@when(u'answer "per week" to your maintenance frequency')
def step_impl(context):
    raise NotImplementedError(u'STEP: When answer "per week" to your maintenance frequency')


@when(u'answer 0 to your pension received')
def step_impl(context):
    raise NotImplementedError(u'STEP: When answer 0 to your pension received')


@when(u'answer "per week" to your pension frequency')
def step_impl(context):
    raise NotImplementedError(u'STEP: When answer "per week" to your pension frequency')


@when(u'answer 0 to your other income')
def step_impl(context):
    raise NotImplementedError(u'STEP: When answer 0 to your other income')


@when(u'answer "per week" to your other income frequency')
def step_impl(context):
    raise NotImplementedError(u'STEP: When answer "per week" to your other income frequency')


@when(u'I click continue to Your outgoings page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click continue to Your outgoings page')


@when(u'answer 0 to your rent amount')
def step_impl(context):
    raise NotImplementedError(u'STEP: When answer 0 to your rent amount')


@when(u'answer "per week" to your rent schedule')
def step_impl(context):
    raise NotImplementedError(u'STEP: When answer "per week" to your rent schedule')


@when(u'answer 0 to your maintenance payment')
def step_impl(context):
    raise NotImplementedError(u'STEP: When answer 0 to your maintenance payment')


@when(u'answer "per week" to your maintenance payment schedule')
def step_impl(context):
    raise NotImplementedError(u'STEP: When answer "per week" to your maintenance payment schedule')


@when(u'answer 0 to your monthly income contribution order')
def step_impl(context):
    raise NotImplementedError(u'STEP: When answer 0 to your monthly income contribution order')


@when(u'I click continue to review the answers page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click continue to review the answers page')


@when(u'I click reviewed questions')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click reviewed questions')


@then(u'I get confirmed my eligibity is "eligible"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I get confirmed my eligibity is "eligible"')
