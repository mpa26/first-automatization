from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import os
import math

try:
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    # 1) Open page  http://suninjuly.github.io/explicit_wait2.html
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # 2) Wait, when the price will be $100 (wait about 12 seconds)
    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    # 3) Press the button "Book"
    button1 = browser.find_element_by_xpath('//button[@id="book"]')
    button1.click()
    # 4) Solve an already known math problem
    x_element = browser.find_element_by_css_selector('span[id="input_value"]')
    x = x_element.text
    result = calc(x)
    # 5) Enter the answer in the text box
    input = browser.find_element_by_xpath('//input[@id="answer"]')
    input.send_keys(result)
    # 6) Press the button "Submit"
    button2 = browser.find_element_by_xpath('//button[@id="solve"]')
    button2.click()

finally:
    time.sleep(5)
    try:
        # Print a message to the console
        alert = browser.switch_to_alert()
        print(alert.text)
    finally:
        browser.quit()
