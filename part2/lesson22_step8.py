import os
import time
from math import log, sin

from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('Ivan')

    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('Ivan')

    input3 = browser.find_element_by_name('email')
    input3.send_keys('abc@abc.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'requirements.txt')

    input4 = browser.find_element_by_name('file')
    input4.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(8)
    browser.quit()
