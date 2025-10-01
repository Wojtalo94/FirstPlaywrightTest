import logging
from playwright.sync_api import Page


class BadResponses:
    def __init__(self, page: Page):
        self.page = page
        self._logger = logging.getLogger("BadResponses")
        self.bad_responses = []
        self.page.on("response", self._on_response)

    def _on_response(self, response):
        status = response.status
        if status >= 400:
            self.bad_responses.append({
                "url": response.url,
                "status": status,
                "resource": response.request.resource_type,
            })

    def assert_no_bad_responses(self):
        if self.bad_responses:
            for resp in self.bad_responses:
                self._logger.error(
                    f"Bad response: {resp['status']} "
                    f"[{resp['resource']}] {resp['url']}"
                )
            raise AssertionError(
                f"Invalid HTTP responses found: {self.bad_responses}"
            )
