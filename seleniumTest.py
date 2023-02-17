from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_confirm_yahoo_title():
    browser = webdriver.Chrome()

    browser.get('http://www.yahoo.com')
    time.sleep(3) # Let the user actually see something!
    browser.find_element(By.NAME,"agree").click()
    time.sleep(3) # Let the user actually see something!
    assert 'Yahoo' in browser.title

    elem = browser.find_element(By.NAME, 'p')  # Find the search box
    elem.send_keys('Silhouette America' + Keys.RETURN)

    time.sleep(5) # Let the user actually see something!

    browser.quit()