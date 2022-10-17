from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestAmazon:
    search_words = ('palm oil', 'dress', 'cars', 'flights', 'shoes for women','shoes for men', 'laptops', 'iphone 13', 'cake')

    driver = ''  

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver.exe")
        self.driver.maximize_window(); 
        self.driver.implicitly_wait(100)
        self.driver.get("https://www.amazon.com/")

    @pytest.mark.parametrize('search_query', search_words) 
    # items.
    def test_amazon_search_items(self, search_query):
        search = self.driver.find_element(By.ID, 'twotabsearchtextbox')
        search.send_keys(search_query, Keys.ENTER)

        expected_text = f'\"{search_query}\"'
        actual_text = self.driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

        assert expected_text == actual_text, f'Error. Expected text: {expected_text}, but actual text: {actual_text}'

    def teardown_method(self): 
        self.driver.quit()
