import pytest


@pytest.fixture()
def empty_str():
    return str()


@pytest.fixture()
def not_empty_str():
    return "string"


def test_empty_str_len(empty_str):
    assert len(empty_str) == 0


def test_not_empty_str_more_than_zero(not_empty_str):
    assert len(not_empty_str) == 6


def test_starts_with_symbols(not_empty_str):
    assert not_empty_str.startswith("str")
    assert not not_empty_str.startswith("qwe")


def test_letter_in_string(not_empty_str):
    assert "s" in not_empty_str
    assert "q" not in not_empty_str


def test_upper(not_empty_str):
    assert not_empty_str.upper() == "STRING"


def test_capitalize(not_empty_str):
    assert not_empty_str.capitalize() == "String"
