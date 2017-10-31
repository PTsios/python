

class GroupHelper:


    def __init__(self, app):
        self.app = app


    def open_group_page(self):
        # open group page
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
           wd.find_element_by_link_text("groups").click()


    def create_new(self, group):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        wd.find_element_by_xpath("/html/body/div/div[4]/form/input[2]").click()
        self.return_to_group_page()


    def fill_group_form(self, group):
        # fill group form
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def return_to_group_page(self):
        # return to group page
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_link_text("group page")) > 0):
           wd.find_element_by_link_text("group page").click()


    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_xpath("/html/body/div/div[4]/form/span[1]/input").click()
        self.selecting_edit_group()
        self.fill_group_form(new_group_data)
        self.submit_update()
        self.return_to_group_page()


    def submit_update(self):
        #submit update
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[4]/form/input[3]").click()


    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.selecting_first_group()
        self.submit_deleting_first_group()
        self.return_to_group_page()


    def selecting_edit_group(self):
        #select edit button
        wd = self.app.wd
        wd.find_element_by_name("edit").click()


    def submit_deleting_first_group(self):
        # submit deletion
        wd = self.app.wd
        wd.find_element_by_name("delete").click()


    def selecting_first_group(self):
        # select first group
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()


    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))



