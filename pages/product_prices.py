from playwright.sync_api import Page

class ProductPrice:
    def __init__(self, page: Page) -> None:
        self.page = page

    def price_filter(self):
        self.page.locator("select.product_sort_container").select_option('hilo')


    def get_all_products_price(self):
        item_prices = self.page.locator(".inventory_item_price").all_text_contents()
        return [float(p.replace("$", "")) for p in item_prices]

    