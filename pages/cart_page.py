from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_items = page.locator(".cart_item")
        self.checkout = page.locator("#checkout")

    def get_cart_items_count(self):
        return self.cart_items.count()
    
    def proceed_to_checkout(self):
        self.checkout.click()


