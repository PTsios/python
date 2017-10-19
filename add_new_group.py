# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app():
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

class add_new_group(app):
    def setUp(self):
        self.app = Application()

def test_add_new_group(app):
    success = True
    app.login(username="admin", password="secret")
    app.creation_new_group(Group(name="1111111", header="22222", footer="33333"))
    app.logout()
    app.assertTrue(success)
