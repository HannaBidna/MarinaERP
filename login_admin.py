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
    #time.sleep(3)
    hname = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div[1]/input")
    hname.send_keys("ex2_admin")

    hpassword = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div[2]/div[2]/input")
    hpassword.send_keys("devtest")

    hbtlogin = driver.find_element(By.CSS_SELECTOR, "#root > div._wrapper_igwh0_1 > div > div._loginElements_igwh0_27 > div._wrapper_oj2b3_1.undefined._lightBlue_oj2b3_80")
    hbtlogin.click()
    time.sleep(5)

def test_add_purchaser(driver):

    hbtnusers = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[2]/a[3]")
    hbtnusers.click()
    time.sleep(5)
    hbtnadd = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div")
    hbtnadd.click()
    time.sleep(3)
    hlogin = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[1]/div[1]/input")
    hlogin.send_keys("tester_purchaser")
    huser_name = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[2]/div[1]/input")
    huser_name.send_keys("Tester")
    huser_surname = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[3]/div[1]/input")
    huser_surname.send_keys("Purchaser")
    huser_email = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[1]/div[2]/input")
    huser_email.send_keys("1@test.com")
    hpassword = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[3]/div[2]/input")
    hpassword.send_keys("testtest")
    #role1 = Select(driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[2]/div[2]/div[2]"))
    #role1.select_by_value("Purchaser")
    #time.sleep(2)
    #hcheckbox = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[4]/div/div/div/svg")
    #hcheckbox.click()
    #hship_choice = driver.find_element((By.XPATH,""))
    hbtcreate = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[5]/div[2]")
    hbtcreate.click()
    time.sleep(2)

def test_add_manager(driver):
    #hbtnusers = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[2]/a[3]")
    #hbtnusers.click()
    #time.sleep(5)
    hbtnadd = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div")
    hbtnadd.click()
    time.sleep(3)
    hlogin = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[1]/div[1]/input")
    hlogin.send_keys("tester_manager")
    huser_name = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[2]/div[1]/input")
    huser_name.send_keys("Tester")
    huser_surname = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[3]/div[1]/input")
    huser_surname.send_keys("Manager")
    huser_email = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[1]/div[2]/input")
    huser_email.send_keys("2@test.com")
    roles = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[2]/div[2]/div[2]/div")
    roles.click()
    time.sleep(2)
    role = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[2]/div[2]/div[4]/div[4]")
    role.click()
    time.sleep(3)
    hpassword = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[3]/div[2]/input")
    hpassword.send_keys("testtest")
    time.sleep(5)
    #hcheckbox = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[4]/div/div/div/svg")
    #hcheckbox.click()
    #hship_choice = driver.find_element((By.XPATH,""))
    hbtcreate = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[5]/div[2]")
    hbtcreate.click()
    time.sleep(5)


def test_add_fleet(driver):
    #hbtnusers = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div[2]/a[3]")
    #hbtnusers.click()
    #time.sleep(5)
    hbtnadd = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div")
    hbtnadd.click()
    time.sleep(3)
    hlogin = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[1]/div[1]/input")
    hlogin.send_keys("tester_fleet")
    huser_name = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[2]/div[1]/input")
    huser_name.send_keys("Tester")
    huser_surname = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[3]/div[1]/input")
    huser_surname.send_keys("Fleet")
    huser_email = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[1]/div[2]/input")
    huser_email.send_keys("3@test.com")
    roles = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[2]/div[2]/div[2]/div")
    roles.click()
    time.sleep(2)
    role = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[2]/div[2]/div[4]/div[5]")
    role.click()
    time.sleep(3)
    hpassword = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[3]/div[2]/input")
    hpassword.send_keys("testtest")
    time.sleep(5)
    #hcheckbox = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[4]/div/div/div/svg")
    #hcheckbox.click()
    #hship_choice = driver.find_element((By.XPATH,""))
    hbtcreate = driver.find_element(By.XPATH, "/html/body/div/div[4]/div[2]/div[5]/div[2]")
    hbtcreate.click()
    time.sleep(5)
