# -*- coding: utf-8 -*-
import pytest

from contacts import Contact
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_new_blank_contact(app):
    app.login( username="admin", password="secret")
    app.adding_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="",company="", address="",home="",email=""))
    app.logout()


def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.adding_new_contact(Contact(firstname="Pavel", middlename="Notallowed", lastname="Tsios", nickname="raynalds", title="QA", company="devhouse", address="Russia. Stavropol", home="9175265472", email="pavel.tsios@devhouese.pro"))
    app.logout()
