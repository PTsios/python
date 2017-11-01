from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contacts import ContactHelper


class Application:
    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False})
       # self.wd.implicitly_wait(5) use for dynamic elements
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contacts = ContactHelper(self)


    def open_home_page(self):
        # open home page
        wd = self.wd
        if not (wd.current_url.endswith("addressbook/index.php") and (len(wd.find_elements_by_name("user")) and len(wd.find_elements_by_name("pass"))) > 0):
                wd.get("http://localhost/addressbook/index.php")


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False


    def destroy(self):
        self.wd.quit()