class LoginPageLocators:
    EMAIL = "#email"
    PASSWORD = "#password"
    LOGIN_BUTTON = "#login"

    MFA_CODE = "#mfa-code"
    MFA_VERIFY = "#verify-mfa"


class AccountPageLocators:
    BANK_ROUTING = "#bank-routing"
    BANK_ACCOUNT = "#bank-account"
    BANK_SAVE = "#bank-save"

    CARD_NAME = "#card-holder"
    CARD_NUMBER = "#card-number"
    CARD_EXP_MONTH = "#card-exp-month"
    CARD_EXP_YEAR = "#card-exp-year"
    CARD_CVC = "#card-cvc"
    CARD_SAVE = "#card-save"

    BANK_SAVED_INFO = "[data-testid='bank-saved-info']"
    PAYMENT_SAVED_INFO = "[data-testid='payment-saved-info']"