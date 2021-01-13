import pytest


@pytest.fixture()
def empty_dict():
    return dict()


@pytest.fixture()
def not_empty_dict():
    return {1: "123", 2: "456", 3: "789"}


@pytest.mark.parametrize(
    "key, value",
    [(4, "101112"), (5, "131415")]
)
def test_update_dict(empty_dict, key, value):
    new_dict = {key: value}

    empty_dict.update(new_dict)

    assert len(empty_dict) == len(new_dict)
    assert empty_dict[key] == value


def test_unique_key(not_empty_dict):
    new_not_empty_dict = not_empty_dict.copy()
    new_not_empty_dict[1] = "000"
    assert len(new_not_empty_dict) == len(not_empty_dict)
    assert new_not_empty_dict[1] != not_empty_dict[1]


def test_pop_item(not_empty_dict):
    new_not_empty_dict = not_empty_dict.copy()
    dict_item = not_empty_dict.get(1)

    pop_dict_item = new_not_empty_dict.pop(1)

    assert dict_item == pop_dict_item
    assert len(not_empty_dict) > len(new_not_empty_dict)


def test_del(not_empty_dict):
    assert 1 in not_empty_dict
    del not_empty_dict[1]
    assert 1 not in not_empty_dict


def test_clear(not_empty_dict):
    new_not_empty_dict = not_empty_dict.copy()
    new_not_empty_dict.clear()
    assert len(new_not_empty_dict) == 0
