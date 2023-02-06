from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com'

def test_guest_can_add_product(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()