from .pages.product_page import ProductPage
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

def test_guest_can_add_product(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_bucket()
    page.solve_quiz_and_get_code()
    page.check_product_name_add()
    page.check_product_price_add()

