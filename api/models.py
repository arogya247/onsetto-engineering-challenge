"""Data models for API workflows."""
from pydantic import BaseModel


class BankingUpdate(BaseModel):
    routing_number: str
    account_number: str


class PaymentUpdate(BaseModel):
    cardholder_name: str
    card_number: str
    exp_month: int
    exp_year: int
    cvc: str