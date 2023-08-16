from selenium import webdriver
from TestLogin import testlogin
import time


def test_02():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(3)
    TestLogin = testlogin(driver)
    TestLogin.Username('Admin')
    TestLogin.Password('admin123')
    TestLogin.button()
    time.sleep(3)
    TestLogin.Admin()
    time.sleep(3)
    TestLogin.Admin_options()
    time.sleep(3)