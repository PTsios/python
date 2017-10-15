# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class add_new_group(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/index.php")


    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


    def open_group_page(self, wd):
        # open group page
        wd.find_element_by_link_text("groups").click()


    def creation_new_group(self, wd, name, header, footer):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("%s" % name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("%s" % header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("%s" % footer)
        wd.find_element_by_name("submit").click()


    def return_to_group_page(self, wd):
        # return to group page
        wd.find_element_by_link_text("group page").click()


    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()


    def test_add_new_group(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.creation_new_group(wd, name="1111111", header="22222", footer="33333")
        self.return_to_group_page(wd)
        self.logout(wd)
        self.assertTrue(success)


    def test_add_new_blank_group(self):
        success = True
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_group_page(wd)
        self.creation_new_group(wd, name="", header="", footer="")
        self.return_to_group_page(wd)
        self.logout(wd)
        self.assertTrue(success)


    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
