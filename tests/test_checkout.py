from pages.all_items_page import AllItemsPage
from pages.cart_page import CartPage
from pages.checkout_page import Checkout


def test_checkout_flow(logged_in_page):
    all_items = AllItemsPage(logged_in_page)
    cart_page = CartPage(logged_in_page)
    checkout_page = Checkout(logged_in_page)

    all_items.add_multiple_items_to_cart(4)
    assert all_items.get_cart_count() == 4

    all_items.go_to_cart()
    assert cart_page.get_cart_items_count() == 4

    cart_page.proceed_to_checkout()
    checkout_page.enter_checkout_details('Saurabh', 'Kale', '431001')
    checkout_page.finish_checkout()

    assert checkout_page.get_success_msg() == "Thank you for your order!"


