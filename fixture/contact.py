#правка 13.04
from model.contact import Contact
class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add_contact(self, contact):
        # add new contact
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.user_info(contact, wd)
        self.submit_contact()
        self.app.open_home_page()
        self.contact_cache = None

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        # select first contact
        self.select_contact_by_index(index)
        # aprove delete contact
        self.accept_next_alert = True
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # close dialog window
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def edit_first_contact(self):
        self.contact_change_by_index(0)

    def contact_change_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit edition contact
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # submit edition contact
        self.user_info(contact, wd)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def user_info(self, contact, wd):
        # select first contact
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Lena123456")
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Anisimova12")
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Выборгская, 29")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("lena@gmail.com")
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("web.ru")
        wd.find_element_by_name("bday").click()
        wd.find_element_by_xpath(f"//option[@value='{contact.bday}']").click()
        wd.find_element_by_name("bmonth").click()
        if contact.bmonth != '-':
            wd.find_element_by_xpath(f"//option[@value='{contact.bmonth}']").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        # wd.find_element_by_name("update").click()
        # wd.find_element_by_link_text("home page").click()

    def submit_contact(self):
         wd = self.app.wd
         wd.find_element_by_name("submit").click()

    def count_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                firstname = element.find_element_by_xpath("td[3]").text
                lastname = element.find_element_by_xpath("td[2]").text
                # all_phones = cell[5].text.splitlines()
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)

 #  def get_contact_info_from_edit_page(self, index):
 #      wd = self.app.wd
 #      self.open_contact_to_edit_by_index(index)
  #     firstname = wd.find_element_by_name("firstname").get_attribute("value")
  #     lastname = wd.find_element_by_name("lastname").get_attribute("value")
  #     id = wd.find_element_by_name("id").get_attribute("value")
     #   homephone = wd.find_element_by_name("home").get_attribute("value")
  #     workphone = wd.find_element_by_name("work").get_attribute("value")
  #  mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
  #      secondaryhone = wd.find_element_by_name("phone2").get_attribute("value")
  #      return Contact(firstname=firstname, lastname=lastname, id=id,
  #                     homephone=homephone, workphone=workphone, mobilephone=mobilephone, secondaryhone=secondaryhone)
