import time
from math import log, sin

from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/execute_script.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    el1 = browser.find_element_by_id('input_value')
    x = int(el1.text)
    r = log(abs(12*sin(x)))

    el2 = browser.find_element_by_id('answer')
    el2.send_keys(str(r))

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector("[for='robotsRule']")
    radiobutton.click()

    button.click()

finally:
    time.sleep(8)
    browser.quit()
