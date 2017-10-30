from model.contacts import Contact


def test_add_new_blank_contact(app):
    app.contacts.modify_first_contact(Contact(firstname="YOYOYOYOYOYOOY"))
