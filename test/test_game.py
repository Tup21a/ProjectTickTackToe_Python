from src.game import parse_to_ints


def test_parse_to_ints_handles_standard_input():
    # given
    user_input = "1 1"
    # when
    row, column = parse_to_ints(user_input)
    # then
    assert row == 1
    assert column == 1


def test_parse_to_ints_handles_commas():
    user_input = "1, 1"

    row, column = parse_to_ints(user_input)

    assert row == 1
    assert column == 1


def test_parse_to_ints_handles_more_spaces():
    user_input = "1  , 1"

    row, column = parse_to_ints(user_input)

    assert row == 1
    assert column == 1
