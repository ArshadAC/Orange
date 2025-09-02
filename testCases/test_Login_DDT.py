import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObject.CredkartRegistration import Registration_Class
from utilities import XLutils
from utilities.readproperties import Readconfig

class Test_Login_DDT():
    Loginurl = Readconfig.geturl()
    path = "C:\\Users\\HP\\Desktop\\Testing\\CT17\\AutomationProject\\OrangeHRM\\TestData\\Login Data.xlsx"

    def test_login_ddt(self,setup):
        self.driver =setup
        self.tl = Registration_Class(self.driver)
        self.rows =XLutils.rowcount(self.path,"Sheet1")
        print("No of rows in sheet is" + str(self.rows))

        status_list = []
        for r in range(2, self.rows + 1):
            self.email = XLutils.readdata(self.path, "Sheet1", r, 1)
            self.password = XLutils.readdata(self.path,"Sheet1",r, 2)
            self.Exp_Result = XLutils.readdata(self.path, "Sheet1", r, 3)
            self.driver.get(self.Loginurl)
            self.tl.Enter_Email(self.email)
            self.tl.Enter_Password(self.password)
            time.sleep(10)
            self.tl.Click_Login_Button()
            if self.tl.Validate_Login() == "Login Pass":
                if self.Exp_Result == "Pass":
                    status_list.append("Pass")
                    XLutils.writedata(self.path,"Sheet1",r,4,"Pass")
                    self.driver.find_element(By.XPATH,"//a[@role='button']").click()

                    self.driver.find_element(By.XPATH,"//a[normalize-space()='Logout']").click()
                    time.sleep(10)
                    # assert True
                elif self.Exp_Result == "Fail":
                    status_list.append("Fail")
                    XLutils.writedata(self.path,"Sheet1",r,4,"Fail")
                    # assert False

            else:
                if self.Exp_Result == "Pass":
                    status_list.append("Fail")
                    XLutils.writedata(self.path,"Sheet1",r,4,"Fail")
                    # assert False

                elif self.Exp_Result == "Fail":
                    status_list.append("Pass")
                    XLutils.writedata(self.path,"Sheet1",r,4,"Pass")
                    # assert True

        print(status_list)
        # if "Fail" in status_list:
        #     print("Test Fail")
        # else:
        #     print("Test Pass")
