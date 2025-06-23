from selenium import webdriver
from selenium.webdriver.common.by import By

# from logger import get_logger
# logger=get_logger()

class Signin:
     signin="//a[@title='Log in to your customer account']"
     txt_email="email_create"
     txt_account="//span[normalize-space()='Create an account']"
     f_name="customer_firstname"
     l_name="customer_lastname"
     passw="passwd"
     regist="//span[normalize-space()='Register']"

#initiate driver
     def __init__(self,driver):
         self.driver=driver
     def set_signin(self):
         sign=self.driver.find_element(By.XPATH,self.signin)
         sign.click()
     def set_email(self,email):
         mail=self.driver.find_element(By.NAME,self.txt_email)
         mail.send_keys(email)
     def set_count(self,):
         count=self.driver.find_element(By.XPATH,self.txt_account)
         count.click()
     def set_f_name(self,f_name):
         first=self.driver.find_element(By.NAME,self.f_name)
         first.send_keys(f_name)
     def set_l_name(self,l_name):
         last=self.driver.find_element(By.NAME,self.l_name)
         last.send_keys(l_name)
     def set_passw(self,passw):
         keys=self.driver.find_element(By.NAME,self.passw)
         keys.send_keys(passw)
     def set_regist(self):
         reg=self.driver.find_element(By.XPATH,self.regist)
         reg.click()




