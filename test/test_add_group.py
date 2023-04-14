# -*- coding: utf-8 -*-

from model.group import Group
import pytest


testdata = [Group(name="qwertyu", header="qwertyu", footer="qwertyu"),
                Group(name="", header="", footer="")
    ]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    pass
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



