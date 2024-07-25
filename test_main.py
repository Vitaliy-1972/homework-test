import unittest
from main import check_month, reverse, check_auth


class TestMain(unittest.TestCase):
    def test_check_month(self):
        for i, (month, expected) in enumerate([
            (13, 'Некорректный номер месяца'),
            (1, 'Зима'),
            (4, 'Весна'),
            (7, 'Лето'),
            (10, 'Осень')
        ]):
            with self.subTest(i):
                result = check_month(month)
                self.assertEqual(expected, result)

    def test_reveres(self):
        for i, (string, expected) in enumerate([
            ('зима', 'амиз'),
            ('машина', 'анишам')
        ]):
            with self.subTest(i):
                result = reverse(string)
                self.assertEqual(expected, result)

    def test_check_auth(self):
        for i, (login, password, expected) in enumerate([
            ('admin', 'password', 'Добро пожаловать'),
            ('admin', '132345464', 'Доступ ограничен'),
            ('pavel', 'password', 'Доступ ограничен')
        ]):
            with self.subTest(i):
                result = check_auth(login, password)
                self.assertEqual(expected, result)
