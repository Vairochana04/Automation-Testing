import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GoogleSearchBoxTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_box_visible(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        wait = WebDriverWait(driver, 10)
        searchbox = wait.until(EC.visibility_of_element_located((By.NAME, "q")))
        self.assertTrue(searchbox.is_displayed(), "Search box should be displayed")
        print("Search box is visible on Google Chrome")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
