
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestSupplier():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_supplier(self):
    self.driver.get("http://dev.project.ex2.team:6969/purchase/suppliers")
    self.driver.set_window_size(1440, 900)
    self.driver.find_element(By.CSS_SELECTOR, ".\\_select_d3rue_9 .\\_shortDescription_1lq98_1 span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_option_d3rue_57:nth-child(7) span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_wrapper_19f56_1:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_wrapper_170o3_1 > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_wrapper_170o3_1 > input").send_keys("Test Group 1")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_text-700_oj2b3_697").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_lightGreen_oj2b3_242:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_element__active_47pll_17 span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_wrapper_oj2b3_1 > div").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_5l66b_51:nth-child(3) > .\\_wrapper_170o3_1:nth-child(3) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_5l66b_51:nth-child(3) > .\\_wrapper_170o3_1:nth-child(3) > input").send_keys("Test Supplier 1")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_5l66b_51:nth-child(4) > .\\_wrapper_170o3_1:nth-child(1) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_5l66b_51:nth-child(4) > .\\_wrapper_170o3_1:nth-child(1) > input").send_keys("1@1.com")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_lightGreen_oj2b3_242").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_lightGreen_oj2b3_242:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_blue_oj2b3_117 > div").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_5l66b_51:nth-child(3) > .\\_wrapper_170o3_1:nth-child(3) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_5l66b_51:nth-child(3) > .\\_wrapper_170o3_1:nth-child(3) > input").send_keys("Test 2")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_5l66b_51:nth-child(4) > .\\_wrapper_170o3_1:nth-child(1) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_5l66b_51:nth-child(4) > .\\_wrapper_170o3_1:nth-child(1) > input").send_keys("2@2.com")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_lightGreen_oj2b3_242").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_lightGreen_oj2b3_242:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_6wmg2_1:nth-child(2) .\\_lightGreyToBlue_oj2b3_333 div:nth-child(2) > svg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_5l66b_51:nth-child(4) > .\\_wrapper_170o3_1:nth-child(3) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_5l66b_51:nth-child(4) > .\\_wrapper_170o3_1:nth-child(3) > input").send_keys("website.com")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_5l66b_51:nth-child(3) > .\\_wrapper_170o3_1:nth-child(1) > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_5l66b_51:nth-child(3) > .\\_wrapper_170o3_1:nth-child(1) > input").send_keys("Name")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_lightGreen_oj2b3_242 > div").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_lightGreen_oj2b3_242:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_6wmg2_1:nth-child(3) .\\_lightGreyToRed_oj2b3_347 div:nth-child(2) > svg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_lightGreen_oj2b3_242").click()
  
