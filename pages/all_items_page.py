from playwright.sync_api import Page


class AllItemsPage:
    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_buttons = page.locator(".inventory_item button")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_icon = page.locator(".shopping_cart_link")

    def add_multiple_items_to_cart(self, count=3):
        for i in range(count):
            self.add_to_cart_buttons.nth(i).click()

    def get_cart_count(self) -> int:
        return int(self.cart_badge.text_content() or 0)
        
    
    def go_to_cart(self):
        self.cart_icon.click()
