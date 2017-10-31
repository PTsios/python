from model.group import Group


def test_modify__first_group_name(app):
    app.group.modify_first_group(Group(name="44444"))


def test_modify_first_group_header(app):
    app.group.modify_first_group(Group(header="55555"))


def test_modify_first_group_footer(app):
    app.group.modify_first_group(Group(footer="777"))