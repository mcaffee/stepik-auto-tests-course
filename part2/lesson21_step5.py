import time
from math import log, sin

from selenium import webdriver

link = 'http://suninjuly.github.io/math.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    el1 = browser.find_element_by_id('input_value')
    x = int(el1.text)
    r = log(abs(12*sin(x)))

    el2 = browser.find_element_by_id('answer')
    el2.send_keys(str(r))

    el3 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    el3.click()

    el4 = browser.find_element_by_css_selector("[for='robotsRule']")
    el4.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(8)
    browser.quit()
