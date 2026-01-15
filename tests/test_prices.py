from pages.product_prices import ProductPrice

def test_verify_price_hightolow(logged_in_page):
    product_price = ProductPrice(logged_in_page)

    product_price.price_filter()
    ui_price = product_price.get_all_products_price()
    print(ui_price)
    sorted_price = sorted(ui_price, reverse= True)
    print(sorted_price)
    assert ui_price == sorted_price