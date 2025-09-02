import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObject.CredkartRegistration import Registration_Class
from utilities.readproperties import Readconfig


class Test_Login:

    URL = Readconfig.geturl()
    Email = Readconfig.getemail()
    Password = Readconfig.getpassword()

    @pytest.mark.sanity
    def test_Login1(self,setup):
        self.driver= setup
        self.tl = Registration_Class(self.driver)
        time.sleep(5)
        self.tl.Click_Login()
        # self.driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
        self.tl.Enter_Email(self.Email)
        # self.tl.Enter_Email("Rajeshp@gmail.com")
        # self.driver.find_element(By.ID, "email").send_keys("Rajeshp@gmail.com")
        self.tl.Enter_Password(self.Password)
        # self.tl.Enter_Password("Rajesh@123")
        # self.driver.find_element(By.ID, "password").send_keys("Rajesh@123")
        self.tl.Click_Login_Button()
        # self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        # time.sleep(5)

        if self.tl.Validate_Login() == "Login Pass":
            assert True

        else:
            assert False


