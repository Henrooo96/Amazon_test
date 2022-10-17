from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAmazonCart:

    driver = ''

    def setup_method(self):
        self.driver = webdriver.Edge(executable_path="C:\drivers\msedgedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get("https://www.amazon.com/")

    def test_empty_cart(self):
        self.driver.find_element(By.ID, 'nav-cart-count').click()
        actual_text = self.driver.find_element(By.XPATH, "//div[@id='sc-active-cart']//h2").text
        expected_text = 'Your Amazon Cart is empty'
        assert actual_text==expected_text, f"Expected text: {expected_text}, but actual text: {actual_text}"

    def teardown_method(self):
        self.driver.quit()