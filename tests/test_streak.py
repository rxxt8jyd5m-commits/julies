import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Tests that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Tests that a list with no positive numbers returns a streak of 0."""
    assert longest_positive_streak([-1, -2, -3, 0]) == 0

def test_all_positive_numbers():
    """Tests that a list with all positive numbers returns the length of the list."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak():
    """Tests a simple case with a single streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_multiple_streaks():
    """Tests that the function returns the length of the longest streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 0, 1, 2, 3, 4, 5]) == 5

def test_streak_at_beginning():
    """Tests a streak at the beginning of the list."""
    assert longest_positive_streak([1, 2, 3, 0, 4]) == 3

def test_streak_at_end():
    """Tests a streak at the end of the list."""
    assert longest_positive_streak([1, 0, 2, 3, 4, 5]) == 4

def test_zeros_and_negatives():
    """Tests that zeros and negative numbers break the streak."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_long_list():
    """Tests with a longer list."""
    assert longest_positive_streak([1] * 100 + [0] + [1] * 50) == 100

def test_single_element_list():
    """Tests with single element lists."""
    assert longest_positive_streak([1]) == 1
    assert longest_positive_streak([0]) == 0
    assert longest_positive_streak([-1]) == 0

def test_provided_example():
    """Tests the example from the problem description."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3
    assert longest_positive_streak([]) == 0
    assert longest_positive_streak([1, 1, 1]) == 3