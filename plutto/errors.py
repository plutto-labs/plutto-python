"""Module to hold the Plutto custom errors."""
from .constants import GENERAL_DOC_URL


class PluttoError(Exception):
    """Represents the base custom error."""

    def __init__(self, error_data, doc_url=GENERAL_DOC_URL):
        error_type = error_data.get("type")
        error_code = error_data.get("code")
        error_message = error_data.get("message")
        error_param = error_data.get("param")
        message = error_type
        message += f": {error_code}" if error_code else ""
        message += f" ({error_param})" if error_param else ""
        message += f"\n{error_message}"
        message += f"\nCheck the docs for more info: {doc_url}"

        super().__init__(message)


class InvalidRequestError(PluttoError):
    """Represents the invalid request error."""


class BadRequestError(PluttoError):
    """Represent the bad request error."""


class UnprocessableEntityError(PluttoError):
    """Represents the unprocessable entity error."""


class UnauthorizedError(PluttoError):
    """Represents the unauthorized entity error."""


class NotFoundError(PluttoError):
    """Represents the not found error."""


class InternalServerError(PluttoError):
    """Represents the internal server error."""


class AuthenticationError(PluttoError):
    """Represents the authentication error."""
