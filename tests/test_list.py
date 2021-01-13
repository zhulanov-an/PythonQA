import pytest


@pytest.fixture()
def empty_list():
    return list()


@pytest.fixture()
def not_empty_list():
    return [1, 2, 3]


def test_add_item(empty_list):
    item = 1
    next_item = 2

    empty_list.append(item)
    assert len(empty_list) == 1

    empty_list.append(next_item)
    assert len(empty_list) == 2

    assert empty_list[0] == item
    assert empty_list[1] == next_item


@pytest.mark.parametrize(
    "new_list",
    [[1, 2, 3], ["1", "2", "3"], [1, "2", 3]]
)
def test_extend_list_by_items(empty_list, new_list):
    empty_list.extend(new_list)
    assert empty_list == new_list
    for i in range(len(new_list)):
        assert new_list[i] == empty_list[i]


def test_pop_item(not_empty_list):
    last_item = not_empty_list[-1]
    assert not_empty_list.count(last_item) == 1
    not_empty_list.pop()
    assert not_empty_list.count(last_item) == 0


def test_reverse(not_empty_list):
    new_not_empty_list = not_empty_list.copy()
    new_not_empty_list.reverse()
    assert new_not_empty_list != not_empty_list
    assert new_not_empty_list[-1] == not_empty_list[0]
    assert new_not_empty_list[-2] == not_empty_list[1]
    assert new_not_empty_list[-3] == not_empty_list[2]


def test_clear(not_empty_list):
    new_not_empty_list = not_empty_list.copy()
    new_not_empty_list.clear()
    assert len(new_not_empty_list) == 0
