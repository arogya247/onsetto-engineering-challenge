"""Entry point for API workflows."""

from client import APIClient
from config import EMAIL, PASSWORD, MFA_CODE


def main():
    client = APIClient()

    try:
        print("Logging in...")
        client.login(EMAIL, PASSWORD, MFA_CODE)

        print("Updating banking details...")
        banking = client.update_banking(
            routing_number="021000021",
            account_number="1234567890",
        )

        print(
            f"✓ Banking updated: "
            f"{banking['routing_masked']} / {banking['account_masked']}"
        )

        print("Updating payment method...")
        payment = client.update_payment(
            cardholder_name="Test User",
            card_number="4242424242424242",
            exp_month=12,
            exp_year=2028,
            cvc="123",
        )

        print(
            f"✓ Payment updated: "
            f"{payment['card_brand']} ending in {payment['last4']}"
        )

        print("\n🎉 All account updates completed successfully!")

    except Exception as e:
        print(f"\n❌ Error: {e}")

    finally:
        client.close()


if __name__ == "__main__":
    main()