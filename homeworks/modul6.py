from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome('/Users/Karol K/PycharmProjects/chromedriver.exe')
url = 'https://fabrykatestow.pl'

driver.get(url)

# kurstaps = driver.find_element_by_xpath('//*[@id="menu-item-506"]/a')
kurstaps = driver.find_element_by_css_selector('#menu-item-506 > a')
kurstaps.click()

image = driver.find_element_by_css_selector('#content > div > div > div > div > div > div > div > section.elementor-element.elementor-element-6acf69cc.elementor-section-boxed.elementor-section-height-default.elementor-section-height-default.elementor-section.elementor-top-section > div.elementor-container.elementor-column-gap-default > div > div > div > div > section > div > div > div.elementor-element.elementor-element-416070db.elementor-column.elementor-col-50.elementor-inner-column > div > div > div.elementor-element.elementor-element-162580f4.elementor-widget.elementor-widget-image > div > div > img')
actions = ActionChains(driver)
actions.move_to_element(image).perform()

driver.save_screenshot('screenshot.png')

driver.quit()
