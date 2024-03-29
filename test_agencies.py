# Generated by Selenium IDE
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

class TestAgencies():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_agencies(self):
    self.driver.get("http://dev.project.ex2.team:6969/purchase/agencies")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_wrapper_1jx5s_1").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_wrapper_19f56_1:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_wrapper_170o3_1 > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_wrapper_170o3_1 > input").send_keys("Test Agency Group")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_wrapper_1fxy6_1 > div:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_text-700_oj2b3_697 > div").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_lightGreen_oj2b3_242:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_wrapper_oj2b3_1 > div").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_4gkm3_50:nth-child(3) input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_4gkm3_50:nth-child(3) input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_4gkm3_50:nth-child(3) input").send_keys("Test Agency 1")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_lightGreen_oj2b3_242 > div").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_lightGreen_oj2b3_242:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_blue_oj2b3_117 > div").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_4gkm3_50:nth-child(3) input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_4gkm3_50:nth-child(3) input").send_keys("Test Agency 2")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_lightGreen_oj2b3_242 > div").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_lightGreen_oj2b3_242:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_11kxo_1:nth-child(1) .\\_wrapper_oj2b3_1:nth-child(1) div:nth-child(2) > svg").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_4gkm3_50:nth-child(4) > .\\_wrapper_170o3_1 > input").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_4gkm3_50:nth-child(4) > .\\_wrapper_170o3_1 > input").send_keys("1@1.com")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_newPort_16uy1_26").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_newPort_16uy1_26").send_keys("Hambu")
    self.driver.find_element(By.CSS_SELECTOR, ".\\_option_wrapper_1tab5_1:nth-child(2)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_lightGreen_oj2b3_242").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_lightGreen_oj2b3_242:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_row_11kxo_1:nth-child(2) .\\_wrapper_oj2b3_1:nth-child(2) div:nth-child(2) path:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".\\_lightGreen_oj2b3_242").click()
  
