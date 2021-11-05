import time
from math import log, sin

from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/selects1.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    el1 = browser.find_element_by_id('num1')
    v1 = int(el1.text)

    el2 = browser.find_element_by_id('num2')
    v2 = int(el2.text)

    r = v1 + v2

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(r))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(8)
    browser.quit()
