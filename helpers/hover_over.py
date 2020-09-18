from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

def hover_over_element(driver_instance, xpath):
    elem = driver_instance.find_element_by_xpath(xpath)
    hover = ActionChains(driver_instance).move_to_element(elem)
    hover.perform()