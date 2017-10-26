# -*- coding: utf-8 -*-

from model.contacts import Contact


def test_add_new_blank_contact(app):
    app.contacts.adding_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="",company="", address="",home="",email=""))


def test_add_new_contact(app):
    app.contacts.adding_new_contact(Contact(firstname="Pavel", middlename="Notallowed", lastname="Tsios", nickname="raynalds", title="QA", company="devhouse", address="Russia. Stavropol", home="9175265472", email="pavel.tsios@devhouese.pro"))
