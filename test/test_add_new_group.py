# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_new(Group(name="1111111", header="22222", footer="33333"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

def test_add_new_blank_group(app):
    old_groups = app.group.get_group_list()
    app.group.create_new(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
