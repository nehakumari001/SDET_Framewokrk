from selenium.webdriver.chrome import webdriver


def setup_method(self):
    self.driver = webdriver.Chrome()
    self.driver.get("http://www.automationpractice.pl/index.php")
    self.driver.maximize_window()
    self.driver.implicitly_wait(10)

def teardown_method(self):
    self.driver.quit()
