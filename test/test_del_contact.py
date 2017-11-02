from model.contacts import Contact

def test_deleting_contact(app):
    if app.contacts.edit_count() == 0:
        app.contacts.adding_new_contact(Contact(firstname="Pavel", middlename="Notallowed", lastname="Tsios", nickname="raynalds", title="QA", company="devhouse", address="Russia. Stavropol", home="9175265472", email="pavel.tsios@devhouese.pro"))
    old_contactss = app.contacts.get_contactss_list()
    app.contacts.deleting_one_contact()
    new_contactss = app.contacts.get_contactss_list()
    assert len(old_contactss) - 1 == len(new_contactss)
    old_contactss[0:1] = []
    assert old_contactss == new_contactss

