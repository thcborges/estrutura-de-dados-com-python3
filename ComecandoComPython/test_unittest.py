import unittest


def fat(n):
    if n == 0:
        return 1
    return n * fat(n - 1)


def pot(base, exp):
    if exp == 0:
        return 1
    return base * pot(base, exp - 1)


class TestMathMethods(unittest.TestCase):

    def test_pot(self):
        self.assertEqual(1, pot(2, 0))

    def test_fat(self):
        self.assertEqual(24, fat(4))


if __name__ == '__main__':
    unittest.main()
