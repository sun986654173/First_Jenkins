from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class webui:
    def __enter__(self):
        self.driver = webdriver.Chrome()
        return self.driver

    def __exit__(self, exc_type, exc_value, traceback):
        if self.driver:
            self.driver.quit()

    def open_website(self, url):
        self.driver.get(url)
        time.sleep(5)  # 等待页面加载

    def search(self, search_box_id, query):
        search_box = self.driver.find_element(By.ID, search_box_id)
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)
