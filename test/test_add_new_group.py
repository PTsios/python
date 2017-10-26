# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.group.create_new(Group(name="1111111", header="22222", footer="33333"))


def test_add_new_blank_group(app):
    app.group.create_new(Group(name="", header="", footer=""))
