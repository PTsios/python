from model.contacts import Contact


def checking_if_contact_exist(app):
    if app.contacts.edit_count() == 0:
        app.contacts.adding_new_contact(Contact(firstname="Pavel", middlename="Notallowed", lastname="Tsios", nickname="raynalds", title="QA", company="devhouse", address="Russia. Stavropol", home="9175265472", email="pavel.tsios@devhouese.pro"))


def test_modify_first_contact_firstname(app):
    old_contactss = app.contacts.get_contactss_list()
    checking_if_contact_exist(app)
    contact = Contact(firstname="YOYOYOYOYOYOOY", middlename="KEKEKEKEK")
    contact.id = old_contactss[0].id
    app.contacts.modify_first_contact(contact)
    new_contactss = app.contacts.get_contactss_list()
    assert len(old_contactss) == len(new_contactss)
    old_contactss[0] = contact
    assert sorted(old_contactss, key=Contact.id_or_max) == sorted(new_contactss, key=Contact.id_or_max)
