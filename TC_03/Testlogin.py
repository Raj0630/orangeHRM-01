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

    def Main_menu(self):   # If the Main Menu is there it will be passed
        self.driverelement.find_element(By.XPATH, "//*[text()='Admin']")          # Admin Menu
        self.driverelement.find_element(By.XPATH, "//*[text()='PIM']")            # PIM Menu
        self.driverelement.find_element(By.XPATH, "//*[text()='Leave']")          # Leave Menu
        self.driverelement.find_element(By.XPATH, "//*[text()='Time']")           # Time menu
        self.driverelement.find_element(By.XPATH, "//*[text()='Recruitment']")    # Recruitment Menu
        self.driverelement.find_element(By.XPATH, "//*[text()='My Info']")        # My Info Menu
        self.driverelement.find_element(By.XPATH, "//*[text()='Performance']")    # Performance Menu
        self.driverelement.find_element(By.XPATH, "//*[text()='Dashboard']")      # Dashboard Menu
        self.driverelement.find_element(By.XPATH, "//*[text()='Directory']")      # Directory Menu
        self.driverelement.find_element(By.XPATH, "//*[text()='Maintenance']")    # Maintenance Menu
        self.driverelement.find_element(By.XPATH, "//*[text()='Buzz']")           # Buzz Menu
        print("Main Menu are valided")