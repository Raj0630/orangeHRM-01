from selenium import webdriver
from Test_Login import test_login
import time


def test_01():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(5)
    Test_Login = test_login(driver)
    Test_Login.Forgotyourpassword()
    time.sleep(5)
    Test_Login.Username('Admin')
    Test_Login.button()
    time.sleep(5)