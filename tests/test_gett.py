from project_testing_1.gett import get_val

collection = a = {1: 'ok', 'cd': '2', 3: ['v', 4], '5': {'g': 0}}
empty_collection = {}
ok_key = 1
new_key = 0

result = 'ok'
default = 'default'


def test_get_val():
    assert get_val(collection, ok_key, default) == result


def test_get_val_for_default():
    assert get_val(collection, new_key, default) == default
    assert get_val(empty_collection, new_key, default) == default




