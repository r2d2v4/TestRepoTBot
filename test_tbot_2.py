import unittest
import tbot_2_lib


words = ["Что-то тут не так. Попробуй снова.\nИли напиши /help для справки.",
         "Не совсем понимаю о чем ты.\nНапиши /help для справки.",
         "Здесь явно что-то не то.\nПопробуй напиши /help для справки."]

class TestCaseTBot(unittest.TestCase):

    def test_add_number(self):
        self.assertEqual(tbot_2_lib.add_number('2', '3'), 5)
        self.assertEqual(tbot_2_lib.add_number('+2', '+3'), 5)
        self.assertEqual(tbot_2_lib.add_number('-2', '4'), 2)
        self.assertEqual(tbot_2_lib.add_number('-2', '+4'), 2)
        self.assertEqual(tbot_2_lib.add_number('2', '-4'), -2)
        self.assertEqual(tbot_2_lib.add_number('+2', '-4'), -2)
        self.assertEqual(tbot_2_lib.add_number('-2', '-3'), -5)
        self.assertIn(tbot_2_lib.add_number('abc', '15'), words)
        self.assertIn(tbot_2_lib.add_number('--15', '++15'), words)

    def test_add_number_float(self):
        self.assertEqual(tbot_2_lib.add_number('1.1', '1.9'), 3.0)
        self.assertEqual(tbot_2_lib.add_number('+1.1', '+1.9'), 3.0)
        self.assertEqual(tbot_2_lib.add_number('-1.1', '2.1'), 1.0)
        self.assertEqual(tbot_2_lib.add_number('-1.1', '+2.1'), 1.0)
        self.assertEqual(tbot_2_lib.add_number('1.1', '-9.1'), -8.0)
        self.assertEqual(tbot_2_lib.add_number('+1.1', '-9.1'), -8.0)
        self.assertEqual(tbot_2_lib.add_number('-1.1', '-1.9'), -3.0)

    def test_add_number_float_2(self):
        self.assertEqual(tbot_2_lib.add_number('1,1', '1,9'), 3.0)
        self.assertEqual(tbot_2_lib.add_number('+1,1', '+1,9'), 3.0)
        self.assertEqual(tbot_2_lib.add_number('-1,1', '2,1'), 1.0)
        self.assertEqual(tbot_2_lib.add_number('-1,1', '+2,1'), 1.0)
        self.assertEqual(tbot_2_lib.add_number('1,1', '-9,1'), -8.0)
        self.assertEqual(tbot_2_lib.add_number('+1,1', '-9.1'), -8.0)
        self.assertEqual(tbot_2_lib.add_number('-1,1', '-1,9'), -3.0)

    def test_add_number_float_3(self):
        self.assertEqual(tbot_2_lib.add_number('1,1', '1.9'), 3.0)
        self.assertEqual(tbot_2_lib.add_number('+1.1', '+1,9'), 3.0)
        self.assertEqual(tbot_2_lib.add_number('-1,1', '2.1'), 1.0)
        self.assertEqual(tbot_2_lib.add_number('-1.1', '+2,1'), 1.0)
        self.assertEqual(tbot_2_lib.add_number('1,1', '-9.1'), -8.0)
        self.assertEqual(tbot_2_lib.add_number('+1.1', '-9.1'), -8.0)
        self.assertEqual(tbot_2_lib.add_number('-1,1', '-1.9'), -3.0)

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
