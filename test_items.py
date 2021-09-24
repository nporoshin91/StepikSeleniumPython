import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def test_basket_button_is_displayed(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    button = WebDriverWait(browser, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, "btn-add-to-basket")))
    assert button, "Could not locate 'Add to basket' button"
