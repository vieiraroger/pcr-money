import unittest

from src.pcr_money.money import Money

class TestMoney(unittest.TestCase):

    def test_apply_round(self):
        m1 = Money(10.789, 3)
        m1.applyRound(3)
        self.assertEqual(m1.value, 10.789)
        self.assertEqual(m1.decimals, 3)
        m1.applyRound(2)
        self.assertEqual(m1.value, 10.79)
        self.assertEqual(m1.decimals, 2)
        m1.applyRound(1)
        self.assertEqual(m1.value, 10.8)
        self.assertEqual(m1.decimals, 1)
        m1.applyRound(0)
        self.assertEqual(m1.value, 11)
        self.assertEqual(m1.decimals, 0)


    def test_sum_money(self):
        m1 = Money(10.77, 2)
        m2 = Money(123.456, 3)
        m3 = m1 + m2
        self.assertEqual(m3.value, 10.77 + 123.456)
        self.assertEqual(m3.decimals, 3)


    def test_handle_value_round(self):
        self.assertEqual(Money.handle_value(10.777, 2 , 'round'), 10.78)
        self.assertEqual(Money.handle_value(10.773, 2 , 'round'), 10.77)
        self.assertEqual(Money.handle_value(10.77, 2 , 'round'), 10.77)


    def test_handle_value_truncation(self):
        self.assertEqual(Money.handle_value(10.777, 2 , 'truncation'), 10.77)
        self.assertEqual(Money.handle_value(10.773, 2 , 'truncation'), 10.77)
        self.assertEqual(Money.handle_value(10.77, 2 , 'truncation'), 10.77)


    def test_handle_value_floor(self):
        self.assertEqual(Money.handle_value(10.777, 2 , 'floor'), 10.77)
        self.assertEqual(Money.handle_value(10.773, 2 , 'floor'), 10.77)
        self.assertEqual(Money.handle_value(10.77, 2 , 'floor'), 10.77)

    def test_handle_value_ceil(self):
        self.assertEqual(Money.handle_value(10.777, 2 , 'ceil'), 10.78)
        self.assertEqual(Money.handle_value(10.773, 2 , 'ceil'), 10.78)
        self.assertEqual(Money.handle_value(10.77, 2 , 'ceil'), 10.77)


if __name__ == '__name__':
    unittest.main()