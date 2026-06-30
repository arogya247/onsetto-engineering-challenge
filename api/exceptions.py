"""Custom exceptions for API workflows."""
class APIError(Exception):
    """Base API exception."""


class AuthenticationError(APIError):
    """Authentication failed."""


class ValidationError(APIError):
    """Invalid request."""


class RateLimitError(APIError):
    """Too many requests."""


class ServerError(APIError):
    """Server returned an error."""