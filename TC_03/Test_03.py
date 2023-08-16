from selenium import webdriver
from Testlogin import testlogin
import time


def test_03():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    time.sleep(3)
    Testlogin = testlogin(driver)
    Testlogin.Username('Admin')
    Testlogin.Password('admin123')
    Testlogin.button()
    time.sleep(3)
    Testlogin.Main_menu()
    time.sleep(3)