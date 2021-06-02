#from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR
from math import ceil, floor

class Money():

    def __init__(self, value=0.0, decimals=2, coin_name='U$', method='round'):
        self.decimals = decimals
        self.coin_name = coin_name
        self.value = self.handle_value(value, decimals, method)


    @staticmethod
    def handle_value(value, decimals, method):
        _round_methods = {
            'round' : lambda value, decimals: round(value, decimals),
            'truncation': lambda value, decimals: int(value),
            'ceil' : lambda value, decimals: ceil(value),
            'floor' : lambda value, decimals: floor(value)
        }
        #value = Decimal(str(value))
        return float(_round_methods[method](value, decimals))

    def __add__(self, other):
        if other.decimals > self.decimals:
            decimal = other.decimals
        else:
            decimal = self.decimals
        return Money((self.value + other.value), decimals=decimal)

    def __sub__(self, other):
        if other.decimals > self.decimals:
            decimal = other.decimals
        else:
            decimal = self.decimals
        return Money((self.value - other.value), decimals=decimal)

    def applyRound(self, decimals, method='round'):
        self.decimals = decimals
        self.value = self.handle_value(self.value, decimals, method)


    def __str__(self):
        return self.coin_name + str(self.money)


    def __repr__(self):
        return f"<Money {self.value}>"
