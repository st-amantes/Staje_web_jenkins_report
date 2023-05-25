import string
from dataclasses import dataclass
from random import random

from selene import browser, command


@dataclass
class FormRegistration:
    def button_registration(self):
        browser.element('[data-qa="auth-button"]').click()
    def fiel_email(self,value):
        browser.element('[data-qa="reset-password-email-input"]').click().send_keys(value)
    def fiel_pasword(self,pasword):
        browser.element('[data-qa="auth-password-input"]').click().send_keys(pasword)

    def repat_pasword(self, pasword):
        browser.element('[data-qa="reset-password-confirm-password-input"]').click().send_keys(pasword)

    def button_sign(self):
        browser.element('[data-qa="sign-in-button"]').perform(command.js.scroll_into_view)
        browser.element('[data-qa="sign-in-button"]').click()

    def confirm_code(self, confirm_pasword):
        browser.element('[data-qa="reset-password-phone-code-input"]').click().send_keys(confirm_pasword)

    def confirm_button(self):
        browser.element('[data-qa="sign-in-button"]').click()
    @staticmethod
    def generate_email(length):
        letters_and_digits = string.ascii_letters + string.digits
        result = ''.join(random.choice(letters_and_digits) for i in range(length))
        return f"{result}@example.com"