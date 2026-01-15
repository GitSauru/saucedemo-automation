def test_successful_login(logged_in_page):
    assert logged_in_page.locator("text= Swag Labs")    