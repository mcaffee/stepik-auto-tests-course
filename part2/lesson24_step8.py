import os
import time
from math import log, sin

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


link = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get(link)

    h5 = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    span = browser.find_element_by_id('input_value')
    x = int(span.text)
    r = log(abs(12*sin(x)))

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(str(r))

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(8)
    browser.quit()
