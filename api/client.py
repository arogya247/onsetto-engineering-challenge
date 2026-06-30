import httpx

from config import API_BASE, TIMEOUT


class APIClient:
    def __init__(self):
        self.client = httpx.Client(
            base_url=API_BASE,
            timeout=TIMEOUT,
        )
        self.token = None

    def login(self, email: str, password: str, mfa_code: str):
        """Authenticate and store the bearer token."""

        # Step 1: Get MFA token
        response = self.client.post(
            "/auth/token",
            json={
                "email": email,
                "password": password,
            },
        )

        self._check_response(response)

        data = response.json()
        mfa_token = data["mfa_token"]

        # Step 2: Verify MFA
        response = self.client.post(
            "/auth/mfa/verify",
            json={
                "mfa_token": mfa_token,
                "code": mfa_code,
            },
        )

        self._check_response(response)

        data = response.json()

        self.token = data["access_token"]

        # Save token for future requests
        self.client.headers.update(
            {
                "Authorization": f"Bearer {self.token}"
            }
        )

        return data
    

    def update_banking(self, routing_number: str, account_number: str):
        """Update the user's banking details."""

        response = self.client.put(
            "/account/banking",
            json={
                "routing_number": routing_number,
                "account_number": account_number,
            },
        )

        self._check_response(response)

        return response.json()
    

    def update_payment(
        self,
        cardholder_name: str,
        card_number: str,
        exp_month: int,
        exp_year: int,
        cvc: str,
    ):
        """Update the user's payment method."""

        response = self.client.put(
            "/account/payment",
            json={
                "cardholder_name": cardholder_name,
                "card_number": card_number,
                "exp_month": exp_month,
                "exp_year": exp_year,
                "cvc": cvc,
            },
        )

        self._check_response(response)

        return response.json()
    

    def _check_response(self, response: httpx.Response):
        if response.status_code == 400:
            raise Exception(f"Validation Error: {response.text}")

        if response.status_code == 401:
            raise Exception(f"Authentication Error: {response.text}")

        if response.status_code == 429:
            raise Exception("Rate limit exceeded.")

        response.raise_for_status()

    def close(self):
        self.client.close()