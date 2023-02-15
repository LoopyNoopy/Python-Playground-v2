import time

from selenium import webdriver



driver = webdriver.Chrome('D:\devDrivers\chromedriver_win32\chromedriver.exe')  # Optional argument, if not specified will search path.

driver.get('https://www.silhouetteamerica.com')

time.sleep(5)  # Let the user actually see something!

driver.find_element(ID="open-search-img").click()
search_box = driver.find_element_by_name('q')

search_box.send_keys('ChromeDriver')

search_box.submit()

time.sleep(5)  # Let the user actually see something!

driver.quit()