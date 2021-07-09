import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

FIREFOX_PATH = r'C:\....\...\...\geckodriver.exe'


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=FIREFOX_PATH)
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("https://www.google.com/intl/en-GB/gmail/about/")
        driver.find_element_by_link_text("Sign in").click()
        driver.find_element_by_id("identifierId").click()
        driver.find_element_by_id("identifierId").clear()
        driver.find_element_by_id("identifierId").send_keys("username")
        driver.find_element_by_xpath("//div[@id='identifierNext']/div/button/span").click()
        driver.implicitly_wait(30)
        time.sleep(2)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("Password")
        driver.find_element_by_xpath("//div[@id='passwordNext']/div/button/div[2]").click()
        driver.find_element_by_xpath(
            "//img[contains(@src,'https://lh3.googleusercontent.com/ogw/ADea4I4cfvVyoD2Rhyfi2vIIvJa5Ss5AZODzaOMEf5cx=s32-c-mo')]").click()
        driver.find_element_by_xpath(
            "//img[contains(@src,'https://lh3.googleusercontent.com/ogw/ADea4I4cfvVyoD2Rhyfi2vIIvJa5Ss5AZODzaOMEf5cx=s32-c-mo')]").click()
        driver.find_element_by_id("gb_71").click()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
