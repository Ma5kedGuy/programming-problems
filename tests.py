import unittest


def smile():
    return ":)"


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(smile(), ":)")


if __name__ == '__main__':
    unittest.main()