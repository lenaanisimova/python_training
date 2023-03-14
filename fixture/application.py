from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper

class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)


    def open_group_page(self):
        # open group page
        wd = self.wd
        wd.get("http://localhost/addressbook/group.php")

    def open_home_page(self):
        # open home page
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")


    def destroy (self):
        self.wd.quit()