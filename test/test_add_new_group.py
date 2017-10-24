# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_new(Group(name="1111111", header="22222", footer="33333"))
    app.session.logout()


def test_add_new_blank_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create_new(Group(name="", header="", footer=""))
    app.session.logout()