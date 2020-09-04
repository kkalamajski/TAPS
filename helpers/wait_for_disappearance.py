from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

def wait_for_invisibility_of_element(inv_driver_instance, xpath, time_to_wait=8):
    inv_element = WebDriverWait(inv_driver_instance, time_to_wait).until(EC.invisibility_of_element_located(By.XPATH, xpath))
    return inv_element