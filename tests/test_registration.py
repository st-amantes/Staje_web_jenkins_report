from selene import browser
from selene.support.shared import browser
from locators.base_page_form_registration import FormRegistration


def test_open():
    form_reg = FormRegistration()
    browser.open('auth')
    form_reg.button_registration()
    form_reg.fiel_email("evit.vit@gmail.com")
    form_reg.fiel_pasword("Ditalive121")
    form_reg.repat_pasword("Ditalive121")
    form_reg.button_sign()
    form_reg.confirm_code("7777")
    form_reg.confirm_button()




