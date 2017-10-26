# -*- coding: utf-8 -*-

from model.group_modification import Group_modification

def test_group_modification(app):
    app.group.modificate_first_group(Group_modification("44444", "55555", "66666"))


