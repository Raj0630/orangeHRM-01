from selenium.webdriver.common.by import By


class test_login:
    def __init__(self, driver):
        self.driverelement = driver

    def Forgotyourpassword(self):
        self.driverelement.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']").click()


    def Username(self, Username):
        self.driverelement.find_element(By.NAME, 'username').send_keys(Username)

    def button(self):
        self.driverelement.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--large oxd-button--secondary orangehrm-forgot-password-button orangehrm-forgot-password-button--reset']").click()