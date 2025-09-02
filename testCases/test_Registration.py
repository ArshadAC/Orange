import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObject.CredkartRegistration import Registration_Class

class Test_Registration:

    def test_Registration_credkart(self,setup):
        self.driver = setup
        self.rc = Registration_Class(self.driver)
        self.rc.Click_Register()
        self.rc.Enter_Name("Pooja")
        self.rc.Enter_Email("Pooja5@gmail.com")
        self.rc.Enter_Password("Pooja@123")
        self.rc.Enter_ConfirmPassowrd("Pooja@123")
        self.rc.Click_Register_Button()
        time.sleep(5)

        if self.rc.Validate_Registration() == "Registration Pass":
            assert True

        else:
            assert False