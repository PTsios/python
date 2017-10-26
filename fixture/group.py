

class GroupHelper:

    def __init__(self, app):
        self.app = app


    def open_group_page(self):
        # open group page
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()


    def create_new(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("%s" % group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("%s" % group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("%s" % group.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        # return to group page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()


    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.selecting_first_group(wd)
        self.submit_deleting_first_group(wd)
        self.return_to_group_page()


    def modificate_first_group(self, group_modification):
        wd = self.app.wd
        self.open_group_page()
        self.selecting_first_group(wd)
        self.selecting_edit_group(wd)
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys("%s" % group_modification.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys("%s" % group_modification.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys("%s" % group_modification.footer)
        wd.find_element_by_name("update").click()
        self.return_to_group_page()



    def selecting_edit_group(self, wd):
        #select edit button
        wd.find_element_by_name("edit").click()


    def submit_deleting_first_group(self, wd):
        # submit deletion
        wd.find_element_by_name("delete").click()


    def selecting_first_group(self, wd):
        # select first group
        wd.find_element_by_name("selected[]").click()


    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_link_text("selected[]"))



