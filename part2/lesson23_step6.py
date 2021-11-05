import os
import time
from math import log, sin

from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.trollface")
    button.click()


    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    span = browser.find_element_by_id('input_value')
    x = int(span.text)
    r = log(abs(12*sin(x)))

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(str(r))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(8)
    browser.quit()
