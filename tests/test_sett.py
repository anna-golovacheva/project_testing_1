from project_testing_1.sett import set_

coll = {"a": {"b": {"c": 0}}}
coll_dif = {"a": {"b": {"c": 0}}}
empty_coll = {}
existing_path = ['a', 'b', 'c']
new_path = ['x', 'y', 'z', 2]
value = 1

result = {"a": {"b": {"c": 1}}}
new_result = {"a": {"b": {"c": 0}}, 'x': {'y': {'z': {2: 1}}}}
empty_result = {'x': {'y': {'z': {2: 1}}}}


def test_set_():
    set_(coll, existing_path, value)
    assert coll == result


def test_set__new_path():
    set_(coll_dif, new_path, value)
    assert coll_dif == new_result


def test_set__empty_coll():
    set_(empty_coll, new_path, value)
    assert empty_coll == empty_result
