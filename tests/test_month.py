from unittest import TestCase


class TestMonth(TestCase):
    def test_month(self):
        from package.sub_package.my_module2 import month

        self.assertEqual(month(1), 'января')
        self.assertEqual(month(2), 'февраля')
        self.assertEqual(month(3), 'марта')
        self.assertEqual(month(4), 'апреля')
        self.assertEqual(month(5), 'мая')
        self.assertEqual(month(6), 'июня')
        self.assertEqual(month(7), 'июля')
        self.assertEqual(month(8), 'августа')
        self.assertEqual(month(9), 'сентября')
        self.assertEqual(month(10), 'октября')
        self.assertEqual(month(11), 'ноября')
        self.assertEqual(month(12), 'декабря')
