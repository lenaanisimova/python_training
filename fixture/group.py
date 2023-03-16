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
        self.fill_group_form(group)
        self.submit_group()
        self.return_group()


    def type(self,field_name,text):
        wd = self.app.wd
        if text is not None:
             wd.find_element_by_name(field_name).click()
             wd.find_element_by_name(field_name).clear()
             wd.find_element_by_name(field_name).send_keys(text)
    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, group):
        wd = self.app.wd
        if group.name is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(group.name)

    def delete_first_group(self):
        wd = self.app.wd
        self.app.open_group_page()
        self.select_first_group()
        #submit deletion
        wd.find_element_by_name("delete").click()
        self.return_group()

    def select_first_group(self):
        # select first group
       wd = self.app.wd
       wd.find_element_by_name("selected[]").click()

    def edit_first_group(self):
        wd = self.app.wd
        self.app.open_group_page()
        #select first group
        wd.find_element_by_name("selected[]").click()
        #submit edition
        wd.find_element_by_name("edit").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[6]").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("qwertyu123456")
        wd.find_element_by_name("update").click()
        self.return_group()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.app.open_group_page()
        self.select_first_group()
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        wd.find_element_by_name("update").click()
        # submit modification
        self.return_group()

