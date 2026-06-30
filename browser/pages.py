"""Page object definitions for browser automation."""
from playwright.sync_api import Page, expect
from locators import LoginPageLocators, AccountPageLocators


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    def login(self, email: str, password: str, mfa_code: str):
        self.page.goto("https://challenge.onsetto.dev/login")

        # Wait for login form
        expect(self.page.locator("#email")).to_be_visible()

        # Fill credentials
        self.page.locator("#email").fill(email)
        self.page.locator("#password").fill(password)

        # Submit
        self.page.get_by_role("button", name="Sign in").click()

        # Wait for MFA
        otp = self.page.locator("input[data-input-otp='true']")
        expect(otp).to_be_visible()

        otp.fill(mfa_code)

        verify = self.page.get_by_role("button", name="Verify")
        expect(verify).to_be_enabled()
        verify.click()

        # Wait until Account link is visible
        expect(
            self.page.get_by_role("link", name="Account")
        ).to_be_visible()


class AccountPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self):
        self.page.get_by_role("link", name="Account").click()

    def update_banking(self, routing: str, account: str):
        self.page.locator(AccountPageLocators.BANK_ROUTING).fill(routing)
        self.page.locator(AccountPageLocators.BANK_ACCOUNT).fill(account)

        self.page.locator(AccountPageLocators.BANK_SAVE).click()

    def update_payment(
        self,
        name: str,
        number: str,
        exp_month: str,
        exp_year: str,
        cvc: str,
    ):
        self.page.locator(AccountPageLocators.CARD_NAME).fill(name)
        self.page.locator(AccountPageLocators.CARD_NUMBER).fill(number)
        self.page.locator(AccountPageLocators.CARD_EXP_MONTH).fill(exp_month)
        self.page.locator(AccountPageLocators.CARD_EXP_YEAR).fill(exp_year)
        self.page.locator(AccountPageLocators.CARD_CVC).fill(cvc)

        self.page.locator(AccountPageLocators.CARD_SAVE).click()


    def verify_banking(self):
        saved_info = self.page.locator(
            AccountPageLocators.BANK_SAVED_INFO
        )

        expect(saved_info).to_be_visible()
        expect(saved_info).to_contain_text("0021")
        expect(saved_info).to_contain_text("7890")


    def verify_payment(self):
        saved_info = self.page.locator(
            AccountPageLocators.PAYMENT_SAVED_INFO
        )

        expect(saved_info).to_be_visible()
        expect(saved_info).to_contain_text("4242")