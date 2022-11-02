import unittest

from leap import count_leap_years


class TestLeap(unittest.TestCase):

    def test_count_leap_years_from_2018_to_2021_returns_one(self):
        # Arrange
        start = 2018
        end = 2021
        expected = 1  # only one leap year in between: 2020

        # Act
        actual = count_leap_years(start, end)  # the actually computed value

        # Assert
        self.assertEqual(expected, actual)
