from playwright.sync_api import Page

class Checkout:
    def __init__(self, page: Page):
        self.page = page

    def enter_checkout_details(self, first, last, zip):
        self.page.fill("#first-name", first)
        self.page.fill("#last-name", last)
        self.page.fill("#postal-code", zip)
        self.page.click("#continue")

    def finish_checkout(self):
        self.page.click("#finish")

    def get_success_msg(self):
        return self.page.text_content(".complete-header")