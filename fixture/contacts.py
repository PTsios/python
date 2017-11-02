from model.contacts import Contact

class ContactHelper:


    def __init__(self, app):
        self.app = app


    def adding_new_contact(self, contacts):
        # add new contact
        wd = self.app.wd
        self.open_new_contact_form()
        self.fill_contact_form(contacts)
        self.submit_new_contact_info()
        self.open_home_page()


    def submit_new_contact_info(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def fill_contact_form(self, contacts):
        wd = self.app.wd
        self.change_contacts_field_value("firstname", contacts.firstname)
        self.change_contacts_field_value("middlename", contacts.middlename)
        self.change_contacts_field_value("lastname", contacts.lastname)
        self.change_contacts_field_value("nickname", contacts.nickname)
        self.change_contacts_field_value("title", contacts.title)
        self.change_contacts_field_value("company", contacts.company)
        self.change_contacts_field_value("address", contacts.address)
        self.change_contacts_field_value("email", contacts.email)
        self.change_contacts_field_value("home", contacts.home)


    def change_contacts_field_value(self, field_name, tekst):
        wd = self.app.wd
        if tekst is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(tekst)


    def open_new_contact_form(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("searchstring")) > 0):
           wd.find_element_by_link_text("add new").click()


    def deleting_one_contact(self):
        wd = self.app.wd
        self.open_home_page()
        self.selecting_first_element()
        self.click_on_delete_button()
        wd.switch_to_alert().accept() #submit deleting


    def click_on_delete_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()


    def selecting_first_element(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[1]/input").click()


    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php") and (len(wd.find_elements_by_link_text("Last name")) and len(wd.find_elements_by_link_text("First name"))) > 0):
            wd.find_element_by_link_text("home").click()


    def choose_first_to_edit(self):
        #choosing first contact and clicking edit
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/table/tbody/tr[2]/td[8]/a/img").click()


    def submit_contact_update(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div[4]/form[1]/input[1]").click()


    def modify_first_contact(self, new_contacts_data):
        wd = self.app.wd
        self.open_home_page()
        self.choose_first_to_edit()
        self.fill_contact_form(new_contacts_data)
        self.submit_contact_update()


    def edit_count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contactss_list(self):
        wd = self.app.wd
        contactss = []
        for element in wd.find_elements_by_css_selector("title.vCard"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contactss.append(Contact(firstname=text, id=id))
        return contactss