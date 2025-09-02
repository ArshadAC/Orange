from selenium import webdriver
from selenium.webdriver.common.by import By

class Registration_Class:
    Button_login_XPATH = (By.XPATH,"//a[normalize-space()='Login']")
    Button_register_XPATH = (By.XPATH,"//a[normalize-space()='Register']")
    Text_Name_ID = (By.ID,"name")
    Text_Email_ID = (By.ID,"email")
    Text_Password_ID = (By.ID,"password")
    Text_Confirm_Password = (By.ID,"password-confirm")
    Button_Register_XPATH = (By.XPATH,"//button[@type='submit']")
    Button_Login_XPATH = (By.XPATH,"//button[@type='submit']")
    Validate_Registration_XPATH = (By.XPATH, "//h2[normalize-space()='CredKart']")

    def __init__(self,driver):
        self.driver = driver

    def Click_Login(self):
        self.driver.find_element(*Registration_Class.Button_login_XPATH).click()

    def Click_Register(self):
        self.driver.find_element(*Registration_Class.Button_register_XPATH).click()

    def Enter_Name(self,name):
        self.driver.find_element(*Registration_Class.Text_Name_ID).send_keys(name)

    def Enter_Email(self,email):
        self.driver.find_element(*Registration_Class.Text_Email_ID).send_keys(email)

    def Enter_Password(self,password):
        self.driver.find_element(*Registration_Class.Text_Password_ID).send_keys(password)

    def Enter_ConfirmPassowrd(self,confirm_password):
        self.driver.find_element(*Registration_Class.Text_Confirm_Password).send_keys(confirm_password)

    def Click_Register_Button(self):
        self.driver.find_element(*Registration_Class.Button_Register_XPATH).click()

    def Click_Login_Button(self):
        self.driver.find_element(*Registration_Class.Button_Login_XPATH).click()

    def Validate_Registration(self):
        try:
            self.driver.find_element(*Registration_Class.Validate_Registration_XPATH)
            print("Registration Pass")
            return "Registration Pass"
        except:
            print("Registration Fail")
            return "Registration Fail"

    def Validate_Login(self):
        try:
            self.driver.find_element(*Registration_Class.Validate_Registration_XPATH)
            print("Login Pass")
            return "Login Pass"
        except:
            print("Login Fail")
            return "Login Fail"
