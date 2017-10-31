from model.contacts import Contact

def test_deleting_contact(app):
    if app.contacts.edit_count() == 0:
        app.contacts.adding_new_contact(Contact(firstname="Pavel", middlename="Notallowed", lastname="Tsios", nickname="raynalds", title="QA", company="devhouse", address="Russia. Stavropol", home="9175265472", email="pavel.tsios@devhouese.pro"))
    app.contacts.deleting_one_contact()
