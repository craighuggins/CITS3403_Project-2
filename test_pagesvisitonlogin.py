# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestPagesvisitonlogin():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_pagesvisitonlogin(self):
    self.driver.get("http://127.0.0.1:5000/login?next=%2F")
    self.driver.set_window_size(550, 680)
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("susan")
    self.driver.find_element(By.ID, "password").send_keys("cat")
    self.driver.find_element(By.ID, "password").send_keys(Keys.ENTER)
    self.driver.find_element(By.LINK_TEXT, "Take Test").click()
    self.driver.find_element(By.ID, "sets").click()
    dropdown = self.driver.find_element(By.ID, "sets")
    dropdown.find_element(By.XPATH, "//option[. = 'xs']").click()
    self.driver.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()
    self.driver.find_element(By.ID, "submit").click()
    self.driver.find_element(By.ID, "Selection_D").click()
    self.driver.find_element(By.CSS_SELECTOR, "form:nth-child(3)").click()
    self.driver.find_element(By.NAME, "SubmitTestBtn").click()
    self.driver.find_element(By.LINK_TEXT, "Results").click()
    self.driver.find_element(By.LINK_TEXT, "Results").click()
    self.driver.find_element(By.LINK_TEXT, "Test History").click()
    self.driver.find_element(By.LINK_TEXT, "Test History").click()
    self.driver.find_element(By.LINK_TEXT, "Authors").click()
    self.driver.find_element(By.LINK_TEXT, "Theme").click()
    self.driver.find_element(By.LINK_TEXT, "Administrator").click()
    self.driver.find_element(By.LINK_TEXT, "Administrator").click()
    self.driver.find_element(By.LINK_TEXT, "Administrator").click()
    self.driver.find_element(By.LINK_TEXT, "Add Questions").click()
    self.driver.execute_script("window.scrollTo(0,377.3333435058594)")
    self.driver.find_element(By.ID, "body").click()
    self.driver.find_element(By.LINK_TEXT, "Administrator").click()
    self.driver.find_element(By.LINK_TEXT, "Add Question Sets").click()
    self.driver.find_element(By.LINK_TEXT, "Administrator").click()
    self.driver.find_element(By.LINK_TEXT, "Add User").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
    self.driver.close()
  
