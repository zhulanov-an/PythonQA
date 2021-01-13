import pytest


@pytest.fixture()
def empty_set():
    return set()


@pytest.fixture()
def not_empty_set():
    return set(range(3))


def test_add_item(empty_set):
    item = 1
    next_item = 2

    empty_set.add(item)
    assert len(empty_set) == 1

    empty_set.add(next_item)
    assert len(empty_set) == 2

    assert item in empty_set
    assert next_item in empty_set


def test_unique_items(not_empty_set):
    new_not_empty_set = not_empty_set.copy()
    item_set = list(not_empty_set)[-1]
    new_not_empty_set.add(item_set)
    assert new_not_empty_set == not_empty_set


def test_pop_item(not_empty_set):
    set_item = list(not_empty_set)[-1]
    assert set_item in not_empty_set

    pop_set_item = not_empty_set.pop()
    assert pop_set_item not in not_empty_set


@pytest.mark.parametrize(
    "new_not_empty_set, item",
    [({1, 2, 3}, 1), ({"1", "2", "3"}, "2"), ({1, "2", 3}, 3)]
)
def test_remove(new_not_empty_set, item):
    assert item in new_not_empty_set
    new_not_empty_set.remove(item)
    assert item not in new_not_empty_set


def test_clear(not_empty_set):
    new_not_empty_set = not_empty_set.copy()
    new_not_empty_set.clear()
    assert len(new_not_empty_set) == 0
