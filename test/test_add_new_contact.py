# -*- coding: utf-8 -*-
from model.contacts import Contact

from model.contacts import Contact


def test_add_new_blank_contact(app):
    old_contactss = app.contacts.get_contactss_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="",company="", address="",home="",email="")
    app.contacts.adding_new_contact(contact)
    new_contactss = app.contacts.get_contactss_list()
    assert len(old_contactss) + 1 == len(new_contactss)
    old_contactss.append(contact)
    assert sorted(old_contactss, key=Contact.id_or_max) == sorted(new_contactss, key=Contact.id_or_max)

#def test_add_new_contact(app):
#    app.contacts.adding_new_contact(Contact(firstname="Pavel", middlename="Notallowed", lastname="Tsios", nickname="raynalds", title="QA", company="devhouse", address="Russia. Stavropol", home="9175265472", email="pavel.tsios@devhouese.pro"))
