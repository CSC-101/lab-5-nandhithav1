import data
import lab5
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.


    # Part 3
    def test_time_add(self):
        time1 = data.Time(10, 20, 30)
        time2 = data.Time(1, 40, 35)
        result = lab5.time_add(time1, time2)
        self.assertEqual(result, data.Time(12, 1, 5))

    def test_time_add_overflow(self):
        time1 = data.Time(23, 59, 59)
        time2 = data.Time(0, 0, 1)
        result = lab5.time_add(time1, time2)
        self.assertEqual(result, data.Time(0, 0, 0))

    # Part 4

    def test_is_descending_true(self):
        self.assertTrue(lab5.is_descending([5.0, 4.0, 3.0, 2.0]))

    def test_is_descending_false(self):
        self.assertFalse(lab5.is_descending([5.0, 5.0, 4.0, 3.0]))

    # Part 5
    def test_largest_between_in_bounds(self):
        self.assertEqual(lab5.largest_between([1, 3, 2, 4], 1, 3), 3)

    def test_largest_between_out_of_bounds(self):
        self.assertIsNone(lab5.largest_between([1, 3, 2, 4], 4, 5))

    # Part 6
    def test_furthest_from_origin(self):
        points = [data.Point(1, 1), data.Point(3, 4), data.Point(0, 0)]
        self.assertEqual(lab5.furthest_from_origin(points), 1)

    def test_furthest_from_origin_empty(self):
        self.assertIsNone(lab5.furthest_from_origin([]))


if __name__ == '__main__':
    unittest.main()
