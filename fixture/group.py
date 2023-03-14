class GroupHelper:
    def __init__(self, app):
        self.app = app

    def return_group(self):
        # return to groups page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def submit_group(self):
        # submit group creation
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def create(self, group):
        # open groups page
        wd = self.app.wd
        #self.app.open_home_page()
        wd.find_element_by_link_text("groups").click()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        self.submit_group()
        self.return_group()

    def delete_first_group(self):
        wd = self.app.wd
        self.app.open_home_page()
        #select first group
        wd.find_element_by_name("selected[]").click()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_group()