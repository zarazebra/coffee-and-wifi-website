from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


class Scraper:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def find_address(self, map_url):
        self.driver.get(map_url)
        time.sleep(5)
        address_tag = self.driver.find_element(By.CSS_SELECTOR, 'div[class="rogA2c "] > div')
        address = address_tag.text
        return address
