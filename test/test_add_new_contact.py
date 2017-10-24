# -*- coding: utf-8 -*-

from model.contacts import Contact


def test_add_new_blank_contact(app):
    app.session.login( username="admin", password="secret")
    app.contacts.adding_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="",company="", address="",home="",email=""))
    app.session.logout()


def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.adding_new_contact(Contact(firstname="Pavel", middlename="Notallowed", lastname="Tsios", nickname="raynalds", title="QA", company="devhouse", address="Russia. Stavropol", home="9175265472", email="pavel.tsios@devhouese.pro"))
    app.session.logout()
