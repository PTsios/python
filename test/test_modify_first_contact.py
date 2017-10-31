from model.contacts import Contact


def test_modify_first_contact_firstname(app):
    if app.contacts.edit_count() == 0:
        app.contacts.adding_new_contact(Contact(firstname="Pavel", middlename="Notallowed", lastname="Tsios", nickname="raynalds", title="QA", company="devhouse", address="Russia. Stavropol", home="9175265472", email="pavel.tsios@devhouese.pro"))
    app.contacts.modify_first_contact(Contact(firstname="YOYOYOYOYOYOOY"))
