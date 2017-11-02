from model.group import Group


def checking_if_group_exists(app): #if there is no group - new will be created
    if app.group.count() == 0:
        app.group.create_new(Group(name="1111111", header="22222", footer="33333"))


def test_modify__first_group_name(app):
    old_groups = app.group.get_group_list()
    checking_if_group_exists(app)
    group = Group(name="44444")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_first_group_header(app):
#    old_groups = app.group.get_group_list()
#    checking_if_group_exists(app)
#    group = Group(header="55555")
#    group.id = old_groups[0].id
#    app.group.modify_first_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_modify_first_group_footer(app):
#    old_groups = app.group.get_group_list()
#    checking_if_group_exists(app)
#    group = Group(footer="777")
#   group.id = old_groups[0].id
#    app.group.modify_first_group(group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = group
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
