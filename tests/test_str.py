import pytest


@pytest.fixture()
def empty_str():
    return str()


@pytest.fixture()
def not_empty_str():
    return "string"


@pytest.mark.parametrize(
    "word, length",
    [("", 0), ("a", 1), ("bc", 2)]
)
def test_str_len(word, length):
    assert len(word) == length


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
