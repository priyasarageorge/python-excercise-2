import unittest
import ex6


class ShortestPath(unittest.TestCase):
    def test_find_a_way_error(self):
        start_point = (0,5)
        end_point = (8,9)
        path = ex6.find_a_way(start_point, end_point)
        self.assertEqual(path, None )

    def test_find_a_way_exists(self):
        start_point = (0,5)
        end_point = (8,5)
        path = ex6.find_a_way(start_point, end_point)
        self.assertEqual(path, [(0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5)])


if ex6 == '_main_':
    unittest.main()
