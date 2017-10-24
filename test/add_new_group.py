# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.creation_new_group(Group(name="1111111", header="22222", footer="33333"))
    app.session.logout()


def test_add_new_blank_group(app):
    app.session.login(username="admin", password="secret")
    app.creation_new_group(Group(name="", header="", footer=""))
    app.session.logout()