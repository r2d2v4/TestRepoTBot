import unittest
import tbot_2_lib


class TestCaseTBot(unittest.TestCase):

    def test_add_number(self):
        self.assertEqual(tbot_2_lib.add_number('2', '3'), 5)
        self.assertEqual(tbot_2_lib.add_number('-2', '4'), 2)
        self.assertEqual(tbot_2_lib.add_number('-2', '-3'), -5)

    def test_add_number_1(self):
        self.assertEqual(tbot_2_lib.add_number('-2', '4'), 2)

    def test_add_number_2(self):
        self.assertEqual(tbot_2_lib.add_number('-2', '-3'), -5)

    def test_bar(self):
        result = tbot_2_lib.bar('+1')
        self.assertEqual(result, 1)
        result = tbot_2_lib.bar('1')
        self.assertEqual(result, 1)
        result = tbot_2_lib.bar('-1')
        self.assertEqual(result, -1)
        result = tbot_2_lib.bar('+1.1')
        self.assertEqual(result, 1.1)
        result = tbot_2_lib.bar('1.1')
        self.assertEqual(result, 1.1)
        result = tbot_2_lib.bar('-1.1')
        self.assertEqual(result, -1.1)
        result = tbot_2_lib.bar('+1,1')
        self.assertEqual(result, 1.1)


if __name__ == 'main':
    unittest.main()
