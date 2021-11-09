"""
Module to hold all the fixtures and stuff that needs to get auto-imported
by PyTest.
"""

from json.decoder import JSONDecodeError

import httpx
import pytest


@pytest.fixture
def patch_http_error(monkeypatch):
    class MockResponse:
        def __init__(self):
            pass

        def json(self):
            return {
                "error": {
                    "type": "api_error",
                    "message": "This is a test error message",
                }
            }

    class MockHTTPError(httpx.HTTPError):
        def __init__(self, message):
            super().__init__(message)
            self.response = MockResponse()

    monkeypatch.setattr(httpx, "HTTPError", MockHTTPError)


@pytest.fixture
def patch_http_client(monkeypatch):
    class MockResponse:
        def __init__(self, method, base_url, url, params, json):
            self._base_url = base_url
            self._params = params
            page = None
            if method == "get" and url[-1] == "s":
                page = int(self._params.pop("page", 1))
            self._page = page
            self._method = method
            self._url = url
            self._json = json

        @property
        def headers(self):
            if self._page is not None and self._page < 10:
                params = "&".join([*self.formatted_params, f"page={self._page + 1}"])
                return {
                    "link": (f"<{self._base_url}/{self._url}?{params}>; " 'rel="next"')
                }
            return {}

        @property
        def formatted_params(self):
            return [f"{k}={v}" for k, v in self._params.items()]

        def raise_for_status(self):
            pass

        def json(self):
            if self._method == "delete":
                raise JSONDecodeError("Expecting value", "doc", 0)
            if self._method == "get" and self._url[-1] == "s":
                return {
                    "resource_doesnt_exists": [
                        {
                            "id": "idx",
                            "method": self._method,
                            "url": self._url,
                            "params": self._params,
                            "json": self._json,
                            "page": self._page,
                    }
                    for _ in range(10)
                ]
            }
            return {
                "resource_doesnt_exist": {
                    "id": "idx",
                    "method": self._method,
                    "url": self._url,
                    "params": self._params,
                    "json": self._json,
                }
            }

