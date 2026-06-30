from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
import os

from pages import LoginPage, AccountPage

load_dotenv()

BANK_ROUTING = "021000021"
BANK_ACCOUNT = "1234567890"

CARD_NAME = "Test User"
CARD_NUMBER = "4242424242424242"
CARD_EXPIRY_MONTH ="12"
CARD_EXPIRY_YEAR = "28"
CARD_CVC = "123"


def main():
    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=False,
            slow_mo=300,
        )

        page = browser.new_page()

        login = LoginPage(page)
        account = AccountPage(page)

        try:
            print("Logging in...")

            login.login(
                email=os.getenv("EMAIL"),
                password=os.getenv("PASSWORD"),
                mfa_code=os.getenv("MFA_CODE"),
            )

            print("Opening Account page...")
            account.open()

            print("Updating banking...")

            account.update_banking(
                routing=BANK_ROUTING,
                account=BANK_ACCOUNT,
            )

            account.verify_banking()

            print("✓ Banking updated.")

            print("Updating payment...")

            account.update_payment(
                name=CARD_NAME,
                number=CARD_NUMBER,
                exp_month=CARD_EXPIRY_MONTH,
                exp_year=CARD_EXPIRY_YEAR,
                cvc=CARD_CVC,
            )

            account.verify_payment()

            print("✓ Payment updated.")

            print("\n🎉 Browser automation completed successfully!")

        finally:
            browser.close()


if __name__ == "__main__":
    main()