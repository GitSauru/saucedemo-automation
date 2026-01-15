from pages.products_page import ProductsPage


def test_verify_sorting_z_to_a(logged_in_page):
    products_page = ProductsPage(logged_in_page)

    products_page.filter_selection()
    ui_names = products_page.get_all_product_names()
    expected_names = sorted(ui_names, reverse= True)

    assert ui_names == expected_names



