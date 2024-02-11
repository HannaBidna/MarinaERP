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
    driver.get("http://dev.project.ex2.team:6016/")
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
   purchbtn = driver.find_element(By.XPATH,  "/html/body/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/a[2]/div")
   purchbtn.click()
   time.sleep(3)
   shipsdd = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[1]/div[4]/div/div"))
   shipsdd.click()
   ship = driver.find_element((By.XPATH, "/html/body/div/div[1]/div[2]/div/div[1]/div[4]/div/div[3]/div[6]"))
   ship.click()

   menu1 = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[1]/div[1]/div/svg")
   menu1.click()
   supp = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div/div[1]/div[1]/div[3]/a[2]")
   supp.click()
