from selenium.webdriver.common.by import By

class testlogin:
    def __init__(self, driver):
        self.driverelement = driver

    def Username(self, Username):
        self.driverelement.find_element(By.NAME, 'username').send_keys(Username)

    def Password(self, Password):
        self.driverelement.find_element(By.NAME, 'password').send_keys(Password)

    def button(self):
        self.driverelement.find_element(By.XPATH, "//button[@type='submit']").click()

    def Admin(self):
        self.driverelement.find_element(By.XPATH, "(//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'])[1]").click()

    def Admin_options(self):   # If the header is there in admin page it will be passed
        self.driverelement.find_element(By.XPATH, "//*[text()='User Management ']")     # User management Header
        self.driverelement.find_element(By.XPATH, "//*[text()='Job ']")                 # Job Header
        self.driverelement.find_element(By.XPATH, "//*[text()='Organization ']")        # Organization Header
        self.driverelement.find_element(By.XPATH, "//*[text()='Qualifications ']")      # Qualifications Header
        self.driverelement.find_element(By.XPATH, "//*[text()='Nationalities']")        # Nationalities Header
        self.driverelement.find_element(By.XPATH, "//*[text()='Corporate Branding']")   # Corporate Branding
        self.driverelement.find_element(By.XPATH, "//*[text()='Configuration ']")       # Configuration
        print("Headers are valided")