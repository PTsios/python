from model.contacts import Contact


def test_modify_first_contact_firstname(app):
    app.contacts.modify_first_contact(Contact(firstname="YOYOYOYOYOYOOY"))
