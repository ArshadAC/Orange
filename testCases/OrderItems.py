# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Edge()
# driver.get("https://automation.credence.in/login")
# driver.maximize_window()
#
# driver.find_element(By.XPATH,"//a[normalize-space()='Login']").click()
# driver.find_element(By.ID,"email").send_keys("Rajeshp@gmail.com")
# driver.find_element(By.ID,"password").send_keys("Rajesh@123")
# driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
# driver.find_element(By.XPATH,"//h3[normalize-space()='Apple Macbook Pro']").click()
# driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
# driver.find_element(By.XPATH,"//a[@class='btn btn-primary btn-lg']").click()
# driver.find_element(By.XPATH,"//h3[normalize-space()='Apple iPad Retina']").click()
# driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
# driver.find_element(By.XPATH,"//a[@class='btn btn-primary btn-lg']").click()
# driver.find_element(By.XPATH,"//h3[normalize-space()='Headphones']").click()
# driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
# time.sleep(10)
#
# l = len(driver.find_elements(By.CSS_SELECTOR,"tbody tr"))
# print(l)
#
# Price_List = []
# for r in range(1,l-2):
#     var = driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(" + str(r)+ ") td:nth-child(4)").text
#     Product_Price = (var[1:])
#     Price_List.append(float(Product_Price))
# print(Price_List)
#
# var2= sum(Price_List)
# Exp_SubTotal = round(var2,2)
# print('Exp_SubTotal', Exp_SubTotal)
# Exp_Tax = round((Exp_SubTotal*0.13),2)
# print('Exp_Tax', Exp_Tax)
# Exp_Total = Exp_SubTotal+Exp_Tax
# print('Exp_Total', Exp_Total)
# #
# Amount_List = []
# for r in range(l-2,l+1):
#     Var = driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(" +str(r)+ ") td:nth-child(4)").text
#     Var2 = (Var[1:])
#     Amounts = Var2.replace(',','')
#     Amount_List.append(float(Amounts))
#
# Act_SubTotal = Amount_List[0]
# print('Act_Subtotal',Act_SubTotal)
# Act_Tax = Amount_List[1]
# print('Act_Tax',Act_Tax)
# Act_Total = Amount_List[2]
# print('Act_Total',Act_Total)
#
# if Exp_SubTotal == Act_SubTotal:
#     print("Subtotal is matched")
# else:
#     print("Subtotal is wrong")
#
# if Exp_Tax == Act_Tax:
#     print("Tax is matched")
# else:
#     print("Tax is wrong")
#
# if Exp_Total == Act_Total:
#     print("Total is matched")
# else:
#     print("Total is wrong")

class Test_Python002:
    def test_mul_004(self):
        a = 3
        b = 5
        mul = a * b
        print(mul)
        if mul == 15:
            assert True  # pass
        else:
            assert False  # fail