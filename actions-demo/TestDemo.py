import unittest
from demo import add


class TestDemo(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(1, 2), 3)


if __name__ == '__main__':
    unittest.main()
