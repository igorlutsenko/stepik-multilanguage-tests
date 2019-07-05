import time
URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_btn_add_to_basket(browser):
    browser.get(URL)
    browser.find_element_by_class_name("btn-add-to-basket")
    time.sleep(10)
