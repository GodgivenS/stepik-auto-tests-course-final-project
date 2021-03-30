from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        assert self.browser.current_url==login_url, "Login url is not corect"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_EMAIL), "Email Login form is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM_PASSWORD), "Password Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_EMAIL), "Email Register form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_PASSWORD), "Password Register form is not presented"
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM_CONFIRM), "Password confirmation Register form is not presented"
