# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from Pages.signin_page import Signin
#
#
# class TestSignin:
#     def test_signin_flow(self):
#         driver=webdriver.Chrome()
#         driver.get("http://www.automationpractice.pl/index.php")
#         driver.maximize_window()
#         driver.implicitly_wait(10)
#         si=Signin(driver)
#         si.set_signin()
#         si.set_email("neha0907@gmail.com")
#         si.set_count()
#         si.set_f_name("Neha")
#         si.set_l_name("Singh")
#         si.set_passw("1234567")
#         si.set_regist()
#
#
#
#     actual_title = driver.title
#     # expected_title = "My Shop"
#     expected_substring = "My Shop"
#
#     print(f"Actual Title: '{actual_title}'")
#
#     # assert actual_title == expected_title, "Test Failed"
#     assert expected_substring in actual_title, f"Test Failed: Expected title to contain '{expected_substring}', got '{actual_title}'"
#     print("Test Passed!")
# import pytest
# from selenium import webdriver
# from Pages.signin_page import Signin
#
# class TestSignin:
#
#     @pytest.fixture(scope="class", autouse=True)
#     def setup(self):
#         self.driver = webdriver.Chrome()
#         self.driver.get("http://www.automationpractice.pl/index.php")
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
#         yield
#         self.driver.quit()
#
#     def test_signin_flow(self):
#         si = Signin(self.driver)
#         si.set_signin()
#         si.set_email("neha0907@gmail.com")
#         si.set_count()
#         si.set_f_name("Neha")
#         si.set_l_name("Singh")
#         si.set_passw("1234567")
#         si.set_regist()
#
#         actual_title = self.driver.title
#         expected_title = "My Shop"
#         print(f"Actual Title: {actual_title}")
#         assert expected_title in actual_title, f"Test Failed: got '{actual_title}'"


import pytest
from selenium import webdriver
from Pages.signin_page import Signin

class TestSignin:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.automationpractice.pl/index.php")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def teardown_method(self):
        self.driver.quit()

    def test_signin_flow(self):
        si = Signin(self.driver)
        si.set_signin()
        si.set_email("nehakumari0709003@gmail.com")
        si.set_count()
        si.set_f_name("Neha")
        si.set_l_name("Singh")
        si.set_passw("1234567")
        si.set_regist()

        actual_title = self.driver.title
        expected_title = "My Shop"
        print(f"Actual Title: {actual_title}")
        assert expected_title in actual_title, f"Test Failed: got '{actual_title}'"
