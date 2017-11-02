from model.group import Group


def checking_if_group_exists(app): #if there is no group - new will be created
    if app.group.count() == 0:
        app.group.create_new(Group(name="1111111", header="22222", footer="33333"))


def test_modify__first_group_name(app):
    old_groups = app.group.get_group_list()
    checking_if_group_exists(app)
    app.group.modify_first_group(Group(name="44444"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_first_group_header(app):
    old_groups = app.group.get_group_list()
    checking_if_group_exists(app)
    app.group.modify_first_group(Group(header="55555"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_first_group_footer(app):
    old_groups = app.group.get_group_list()
    checking_if_group_exists(app)
    app.group.modify_first_group(Group(footer="777"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)