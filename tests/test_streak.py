import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_single_positive():
    """Test a list with a single positive number."""
    assert longest_positive_streak([1]) == 1

def test_single_negative():
    """Test a list with a single negative number."""
    assert longest_positive_streak([-1]) == 0

def test_single_zero():
    """Test a list with a single zero."""
    assert longest_positive_streak([0]) == 0

def test_all_positive():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_all_negative():
    """Test a list with all negative numbers."""
    assert longest_positive_streak([-1, -2, -3, -4, -5]) == 0

def test_all_zeros():
    """Test a list with all zeros."""
    assert longest_positive_streak([0, 0, 0, 0, 0]) == 0

def test_mixed_numbers():
    """Test a list with a mix of positive, negative, and zero values."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_multiple_streaks():
    """Test that the function returns the length of the longest streak."""
    assert longest_positive_streak([1, 2, 0, 1, 2, 3, 0, 1, 2]) == 3

def test_streak_at_beginning():
    """Test a streak at the beginning of the list."""
    assert longest_positive_streak([5, 6, 7, 0, 4]) == 3

def test_streak_at_end():
    """Test a streak at the end of the list."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7]) == 3

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -5, 0, -2]) == 0