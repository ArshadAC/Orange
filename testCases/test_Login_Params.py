import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObject.CredkartRegistration import Registration_Class

class Test_Login_Params:

    def test_Login_Params(self,setup,getdataforlogin):
        self.driver = setup
        self.tl = Registration_Class(self.driver)
        self.tl.Click_Login()
        self.tl.Enter_Email(getdataforlogin[0])
        self.tl.Enter_Password(getdataforlogin[1])
        self.tl.Click_Login_Button()
        status_list=[]
        if self.tl.Validate_Login() == "Registration Pass":
            if getdataforlogin[2] == "Pass":
                status_list.append("Pass")
                # assert True
            elif getdataforlogin[2] == "Fail":
                status_list.append("Fail")
                # assert False

        else:
            if getdataforlogin[2] == "Pass":
                status_list.append("Fail")
                # assert False

            elif getdataforlogin[2] == "Fail":
                status_list.append("Pass")
                # assert True

        if "Fail" in status_list:
            print("Test Fail")
        else:
            print("Test Pass")