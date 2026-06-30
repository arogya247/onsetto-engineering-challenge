"""Configuration helpers for API workflows."""
from dotenv import load_dotenv
import os

load_dotenv()

API_BASE = os.getenv(
    "API_BASE",
    "https://zvyhufnwclhcvmgtqxwp.supabase.co/functions/v1/api-v1",
)

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
MFA_CODE = os.getenv("MFA_CODE", "1234")

TIMEOUT = 20.0