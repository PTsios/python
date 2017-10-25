

def test_deleting_all_contact(app):
    app.session.login( username="admin", password="secret")
    app.contacts.deleting_one_contact()
    app.session.logout()
