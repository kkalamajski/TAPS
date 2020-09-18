from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/Karol202/PycharmProjects/chromedriver.exe')

driver.get('https://google.com')
search_box = driver.find_element_by_name('q')
search_box.send_keys('Selenium')
search_box.submit()
time.sleep(5)
driver.quit()
