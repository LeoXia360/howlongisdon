from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest


class TestPageNav(unittest.TestCase):

    driver = webdriver.Firefox()
    driver.get("http://howlongisdon.pythonanywhere.com")

    def test_about(self):
        # about test
        self.driver.find_element_by_class_name("burger").click()
        time.sleep(5)
        self.driver.find_element_by_id("about-link").click()
        time.sleep(5)
        print self.driver.find_element_by_id("about-text").text
        self.assertEqual(self.driver.find_element_by_id("about-text").text, "about:")

    def test_contact(self):
        # about test
        self.driver.find_element_by_class_name("burger").click()
        time.sleep(5)
        self.driver.find_element_by_id("contact-link").click()
        time.sleep(5)
        print self.driver.find_element_by_id("contact-text").text
        self.assertEqual(self.driver.find_element_by_id("contact-text").text, "contact")

    def test_login(self):
        # about test
        self.driver.find_element_by_class_name("burger").click()
        time.sleep(5)
        self.driver.find_element_by_id("admin-link").click()
        time.sleep(5)
        print self.driver.find_element_by_class_name("admin-buttons").text
        self.assertEqual(self.driver.find_element_by_class_name("admin-buttons").text, "logout")

    # def tearDown(self):
    #     self.driver.quit()


if __name__ == '__main__':
    unittest.main()








