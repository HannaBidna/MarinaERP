from select import select

import pytest
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="module")
def driver():
    print("Init driver")
    driver = Chrome()
    yield driver
    print("Quit driver")
    driver.quit()


def test_login(driver):
    driver.get("http://dev.project.ex2.team:6969/")
    driver.maximize_window()
    hbtnsingup = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div")
    hbtnsingup.click()
    hname = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div[1]/input")
    hname.send_keys("tester_manager")
    hpassword = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div[2]/input")
    hpassword.send_keys("testtest")
    hbtlogin = driver.find_element(By.CSS_SELECTOR, "#root > div._wrapper_igwh0_1 > div > div._loginElements_igwh0_27 > div._wrapper_oj2b3_1.undefined._lightBlue_oj2b3_80")
    hbtlogin.click()
    time.sleep(5)


def test_add(driver):
   driver.get("http://dev.project.ex2.team:6969/purchase/requisitions-board")
   #menubtn = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div")
   #menubtn.click()
   #purchbtn = driver.find_element(By.XPATH,  "/html/body/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/a[2]/div")
   #purchbtn.click()
   #time.sleep(5)
   ships = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[1]/div[4]")
   ships.click()
   ship = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[1]/div[4]/div/div[3]/div[6]")
   ship.click()
   menu1 = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[1]/div[1]/div")
   menu1.click()
   sup = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[1]/div[1]/div[3]/a[2]")
   sup.click()
   time.sleep(5)
   add_group = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[2]/div[1]/div[1]/div[1]")
   add_group.click()
   name_group = driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/div[1]/input")
   name_group.send_keys("Test Group")
   btncreate = driver.find_element(By.XPATH, "/ html / body / div / div[3] / div[3] / div[2] / div[2]")
   btncreate.click()
   donebtn = driver.find_element(By.CSS_SELECTOR, "#root > div._wrapper_150yr_1._z1005_150yr_59 > div._buttons_150yr_52 > div")
   donebtn.click()
   time.sleep(5)
   new_group = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/div[39]")
   new_group.click()
   time.sleep(3)

   driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[1]/div[4]").click()
   time.sleep(3)
   driver.find_element(By.XPATH, "/html/body/div/div[3]/div[3]/div[3]/input").send_keys("Supplier 0")
   time.sleep(3)
   driver.find_element(By.XPATH, "/html/body/div/div[3]/div[4]/div[1]/input").send_keys("Supplier1@test.com")
   driver.find_element(By.XPATH, "/html/body/div/div[3]/div[9]/div[2]").click()
   time.sleep(3)
   donebtn = driver.find_element(By.XPATH, "/html/body/div/div[5]/div[3]/div")
   donebtn.click()


