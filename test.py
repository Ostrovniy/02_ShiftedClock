import unittest
from main import validate_time_string

class ValidInputTime(unittest.TestCase):
    def test_input(self):
        # Корректные входные данные
        self.assertEqual(validate_time_string('12:00'), True)
        self.assertEqual(validate_time_string('00:10'), True)
        self.assertEqual(validate_time_string('12:10'), True)
        self.assertEqual(validate_time_string('23:59'), True)
        self.assertEqual(validate_time_string('24:00'), True)
        self.assertEqual(validate_time_string('24:59'), True)

        # Некорректные часы
        self.assertEqual(validate_time_string("25:00"), False)  # False, 25 не входит в диапазон от 0 до 24
        self.assertEqual(validate_time_string("30:10"), False)  # False, 30 не входит в диапазон от 0 до 24

        # Некорректные минуты
        self.assertEqual(validate_time_string("12:60"), False)  # False, 60 не входит в диапазон от 0 до 59
        self.assertEqual(validate_time_string("23:70"), False)  # False, 70 не входит в диапазон от 0 до 59

        # Некорректные часы и минуты
        self.assertEqual(validate_time_string("25:70"), False)  # False, и часы, и минуты выходят за пределы
        self.assertEqual(validate_time_string("24:61"), False)  # False, 61 не входит в диапазон от 0 до 59 при 24 часах

        # Пограничные случаи
        self.assertEqual(validate_time_string('1:5'), True)    # True, "1:05" также считается валидным
        self.assertEqual(validate_time_string('12:5'), True)   # True, "12:05" также считается валидным
        self.assertEqual(validate_time_string('0:60'), False)  # False, 60 не входит в диапазон

        # Некорректные форматы
        self.assertEqual(validate_time_string(''), False)  # False, пустая строка
        self.assertEqual(validate_time_string('not a time'), False)  # False, некорректный формат строки
        self.assertEqual(validate_time_string('1234'), False)  # False, нет разделителя ":"
        self.assertEqual(validate_time_string('12:345'), False)  # False, некорректный формат минут

if __name__ == '__main__':
    unittest.main()
