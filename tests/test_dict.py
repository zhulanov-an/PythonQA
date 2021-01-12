import pytest


@pytest.fixture()
def empty_dict():
    return dict()


@pytest.fixture()
def not_empty_dict():
    return {1: "123", 2: "456", 3: "789"}


def test_update_dict(empty_dict):
    pair = {4: "101112"}
    next_pair = {5: "131415"}

    empty_dict.update(pair)
    assert len(empty_dict) == 1

    empty_dict.update(next_pair)
    assert len(empty_dict) == 2

    assert empty_dict[4] == "101112"
    assert empty_dict[5] == "131415"


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
    new_not_empty_dict = not_empty_dict.copy()
    assert 1 in not_empty_dict
    del not_empty_dict[1]
    assert 1 not in not_empty_dict


def test_clear(not_empty_dict):
    new_not_empty_dict = not_empty_dict.copy()
    new_not_empty_dict.clear()
    assert len(new_not_empty_dict) == 0
