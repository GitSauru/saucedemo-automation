from playwright.sync_api import Page


class ProductsPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def filter_selection(self):
        self.page.locator("select.product_sort_container").select_option("za")

    def get_all_product_names(self):
        items = self.page.locator("inventory_item_name ").all_text_contents()
        return items
    
    
    
        


    
        
